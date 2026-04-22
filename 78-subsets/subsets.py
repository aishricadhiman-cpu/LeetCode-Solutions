class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        result = []

        def recursion(index,subsets):
            if index >= n:
                result.append(list(subsets))
                return
            subsets.append(nums[index])
            recursion(index + 1,subsets)
            subsets.pop()
            recursion(index + 1, subsets)
        recursion(0, [])
        return result



        
        