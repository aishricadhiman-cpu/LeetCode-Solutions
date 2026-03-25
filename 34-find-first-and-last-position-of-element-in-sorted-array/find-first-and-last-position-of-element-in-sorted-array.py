class Solution(object):

    def lowerbound(self, nums, target):
        n = len(nums)
        lb = -1
        low = 0
        high = n-1
        while low <= high:
            mid = int((low + high)//2)
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else: 
                low = mid + 1
        if lb == -1 or nums[lb] != target:
            lb = -1
        return lb 

    def upperbound(self, nums, target):
        n = len(nums)
        ub = -1
        low = 0
        high = n-1
        while low <= high:
            mid = int((low + high)//2)
            if nums[mid] <= target:
                ub = mid
                low = mid + 1
            else:
                high = mid - 1
        return ub


    def searchRange(self, nums, target):
        
        lb = self.lowerbound(nums, target)
        ub = self.upperbound(nums, target)
        if lb == -1:
            return[-1,-1]
        else:
            return [lb,ub]
