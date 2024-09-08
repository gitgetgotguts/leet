from collections import Counter

strs =["eat","tea","tan","ate","nat","bat"]
class Solution:




    def groupAnagrams(self, strs) :
        Clist = list(map(Counter, strs))
        # lists are unhashable so we use tuples
        # counters are unhashable also
        Fstrs=strs.copy()

        Flist=[]
        for i,str in enumerate(strs):
            if str in Fstrs:
                temp=[]
                for j in range(len(Clist)):
                    if Clist[i]==Clist[j]:
                        temp.append(strs[j])
                        Fstrs.remove(strs[j])


                Flist.append(temp)


        return Flist













print(Solution().groupAnagrams(strs))