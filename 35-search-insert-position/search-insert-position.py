class Solution(object):
    def searchInsert(self, nums, target):
        n= len(nums)
        low = 0
        high = n-1
        lb = n
        while low <= high:
            mid = int((low+high)//2)
            if nums[mid] >= target:
                lb = mid
                high = mid - 1

            else:
                low = mid + 1
        return lb


        