#May 16, 2023
#making an anagram detector, an anagram is a word or phrase that is form when rearranging another word

def anagram(word, comparator):
    if len(word) != len(comparator): return f"{comparator} is not anagram of {word}"
    return "{} is an anagram of {}".format(comparator, word) if all([i for i in comparator if i in word]) else "{} is not an anagram of {}".format(comparator, word)

print()