import numpy as np


class Solution:
    def productExceptSelf(self, nums) :
        if 0 not in nums:
            f = np.prod(nums)
            return [int(f / i) for i in nums]
        else:
            l = len(nums)
            ind = nums.index(0)
            nums.remove(0)
            if 0 in nums:
                return [0 for i in range(l)]
            else:
                end = []
                for i in range(l):
                    if i == ind:
                        end.append(np.prod(nums))
                    else:
                        end.append(0)
                return end
