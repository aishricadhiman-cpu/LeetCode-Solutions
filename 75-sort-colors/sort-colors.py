class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0 
        j = n-1
        k = 0
        while k <= j:
            if nums[k] == 0:
                nums[k],nums[i] = nums[i],nums[k]
                i+=1
                k+=1
            
            elif nums[k] == 1:
                k+=1

            else:
                nums[k],nums[j] = nums[j],nums[k]
                j-=1

        

                