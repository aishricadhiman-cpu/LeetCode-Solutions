class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(0,numRows):
            rows = [1]*(i+1)
            if i>0:
                prev_rows = result[i-1]
                for j in range(1,i):
                    rows[j] = prev_rows[j-1]+ prev_rows[j]
            result.append(rows)
        return result

            
