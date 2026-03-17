class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.n = len(nums)
        self.dict = {}
        for i, num in enumerate(nums):
            self.remain = target - nums[i]

            if self.remain in self.dict:
                return (self.dict[self.remain],i)

            else:
                self.dict[num] = i
        
