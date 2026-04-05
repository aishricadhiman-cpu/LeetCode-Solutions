class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def recurPermute(index):
            if index == len(nums):
                result.append(nums[:])
                return 

            for i in range(index,len(nums)):
                nums[i],nums[index] = nums[index],nums[i]

                recurPermute(index + 1)

                nums[i],nums[index] = nums[index],nums[i]

        recurPermute(0)
        return result



        