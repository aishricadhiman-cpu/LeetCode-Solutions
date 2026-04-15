class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i = 0
        j = n-1
        max_water = 0
        while i < j:
            water = min(height[i],height[j]) * (j-i)
            max_water = max(water,max_water)
        
            if height[i] < height[j]:
                i += 1
            else: 
                j-=1
        return max_water