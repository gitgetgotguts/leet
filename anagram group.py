from collections import Counter

strs =["eat","tea","tan","ate","nat","bat"]
class Solution:




    def groupAnagrams(self, strs) :
        Clist = list(map(Counter, strs))
        # lists are unhashable so we use tuples
        # counters are unhashable also
        # Fstrs=strs.copy()

        Flist=[]
        Dic = {}
        for n,i in enumerate(Clist):
            temp='0'

            keys=list(i.keys())

            keys.sort()


            for j in keys:
                print(j,i[j])
                temp+=j+str(i[j])
            if temp not in Dic.keys():
                Dic[temp]=[strs[n]]
            else:
                Dic[temp].append(strs[n])




        # for i,str in enumerate(strs):
        #     if Flist[i] in Dic.keys():
        #         Dic[Flist[i]].append(str)
        #     else :
        #         Dic[Flist[i]] = [str]









        return list(Dic.values())


print(Solution().groupAnagrams(strs))