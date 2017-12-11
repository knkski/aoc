with open('day4.txt') as f:
    phrases = [l.strip() for l in f.readlines()]


def no_dupes(phrase):
    words = phrase.split(' ')
    return len(words) == len(set(words))


def no_anagrams(phrase):
    words = phrase.split(' ')
    return len(words) == len(set([''.join(sorted(w)) for w in words]))


print(len([phrase for phrase in phrases if no_dupes(phrase)]))
print(len([phrase for phrase in phrases if no_anagrams(phrase)]))
