class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        smax = float('-inf')
        total = 0
        for i in range(0,n):
            total = total + nums[i]
            smax = max(smax,total)
            if total < 0:
                total = 0
        return smax

            

        