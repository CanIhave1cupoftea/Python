#May 16, 2023 3:39pm
#Making an isogram detector, an isogram is a word that has no repeating letters


def isogram(word):
    word = word.lower()
    return f"{word} is an isogram" if all([i for i in word if word.count(i) ==  1]) else f"{word} is not an isogram"

print(("sheEt"))

