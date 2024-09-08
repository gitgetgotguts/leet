class Solution:
        def getLucky(self, s: str, k: int) -> int:


            v=''
            # transform
            for i in s:
                v+=str(ord(i) - 96)

            for i in range(k):

                z = sum([int(x) for x in v])
                v=str(z)
                print('l',v)




            return z

a=Solution()
print(a.getLucky('leetcode',2))

