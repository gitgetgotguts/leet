from collections import Counter

strs =["eat","tea","tan","ate","nat","bat"]
Clist = list(map(Counter, strs))
for i in Clist:
    keys = i.keys()
    print(list(keys).sort())