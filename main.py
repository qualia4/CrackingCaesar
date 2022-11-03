import matplotlib.pyplot as plot

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
letters_frequency = {"a": 8.2, "b": 1.5, "c": 2.8, "d": 4.3, "e": 13, "f": 2.2, "g": 2, "h": 6.1, "i": 7,
                      "j": 0.15, "k": 0.77, "l": 4, "m": 2.4, "n": 6.7, "o": 7.5, "p": 1.8, "q": 0.095, "r": 6,
                      "s": 6.3, "t": 9.1, "u": 2.8, "v": 0.98, "w": 2.4, "x": 0.15, "y": 2, "z": 0.074}


def draw_chart(frequencies):
    plot.plot(frequencies.keys(), frequencies.values())
    plot.xlabel("Letters")
    plot.ylabel("Frequency")
    plot.title("Frequency polygon")
    plot.show()


def count_frequencies(text):
    frequencies = {}
    for el in text:
        if el.isalpha():
            if el.lower() not in frequencies:
                frequencies[el.lower()] = 1
            else:
                frequencies[el.lower()] += 1
    return frequencies


def count_percentage_frequency(frequencies):
    result = {}
    sum = 0
    for el in frequencies.values():
        sum += el
    for el in frequencies:
        frequency = frequencies[el]
        percentage = (frequency / sum) * 100
        result[el] = percentage
    return result


def decrypt(text, key):
    result = ''
    for letter in text:
        if letter.isalpha():
            index = alphabet.index(letter.lower())
            if index - key >= 0:
                result += alphabet[index - key]
            else:
                result += alphabet[(index - key % 26)]
        else:
            result += letter
    return result


def decryptForEvery(text):
    variantes = []
    for key in range(1, 27):
        variantes.append(decrypt(text, key))
    return variantes


def countDifference(text):
    frequencies = count_frequencies(text)
    frequencies = {key: value for key, value in sorted(frequencies.items())}
    frequencies = count_percentage_frequency(frequencies)
    sum = 0
    for key in frequencies.keys():
        sum += abs(frequencies[key] - letters_frequency[key])
    return sum


def allDifferences(variantes):
    sums = []
    for i in range(0, 26):
        sums.append(countDifference(variantes[i]))
    return sums


def findBestKeys(sums):
    keys = []
    for i in range(1, 4):
        minIndex = sums.index(min(sums))
        keys.append(minIndex + 1)
        sums.pop(minIndex)
    return keys


file = open("ForPython6.txt", "r")
text = file.read()
possibleDecryptions = decryptForEvery(text)
differences = allDifferences(possibleDecryptions)
keys = findBestKeys(differences)
print(keys)
decrypted = decrypt(text, keys[0])
freq = count_frequencies(decrypted)
freq = {key: value for key, value in sorted(freq.items())}
frequencies = count_percentage_frequency(freq)
draw_chart(freq)







