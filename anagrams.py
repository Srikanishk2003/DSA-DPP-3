from collections import defaultdict


words = ["gintoki", "ichigo", "luffy", "itadori", "anime", "naruto"]


anagrams = defaultdict(list)


for word in words:
    anagrams[''.join(sorted(word))].append(word)


for anagram in anagrams.values():
    print(' '.join(anagram))