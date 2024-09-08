from collections import Counter

strs =["eat","tea","tan","ate","nat","bat"]
class Solution:
    def groupAnagrams(self, strs) :
        Clist = list(map(Counter, strs))
        # lists are unhashable so we use tuples
        # counters are unhashable also

        Hash = {}
        for i,n in enumerate(strs):
            if Clist[i] in Hash.keys():
                Hash[Clist[i]].append(n)
        else:Hash[Clist[i]] = n
        return Hash.values()
print(Solution().groupAnagrams(strs))