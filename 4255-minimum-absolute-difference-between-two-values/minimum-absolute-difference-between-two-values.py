class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_diff = float('inf')
        k = -1   # last index of 1
        l = -1   # last index of 2

        for i in range(len(nums)):
            if nums[i] == 1:
                k = i
            elif nums[i] == 2:
                l = i
    
            if k != -1 and l != -1:
                diff = abs(k - l)
                min_diff = min(min_diff, diff)

        if min_diff == float('inf'):
            return -1
        return min_diff
        
    
        