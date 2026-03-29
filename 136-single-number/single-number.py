class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        n = len(nums)
        for element in nums:
            dict[element] = dict.get(element,0) + 1

        for k,v in dict.items():
            if v == 1:
                return k


            