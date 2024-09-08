from collections import Counter
nums=[2,1,1,2,1,2,3,4,2,3]
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
count=Counter(nums)
res=[(j,i) for i,j in count.items()]
res.sort(reverse=1)
result=[]
for i in range(k):
    result.append(res[i][1])
print(result)

