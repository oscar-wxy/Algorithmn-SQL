"""
dp
dp(i,j,k+1) if dp(i.j-1,k), dp(i-1,j,k), dp(i-1,j-1,k). actually it's mininum
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        memo = {}
        
        # initialize
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                # dp(i,j,k+1) if dp(i.j-1,k), dp(i-1,j,k), dp(i-1,j-1,k). actually it's mininum
                if matrix[row][col] == '1':
                    memo[(row,col)] = 1
                else:
                    memo[(row,col)] = 0
        
        max_len = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    if row > 0 and col > 0:
                        memo[(row,col)] = min(memo[(row-1,col)],memo[(row,col-1)],memo[(row-1,col-1)]) + 1
                        
                    max_len = max(max_len, memo[(row,col)])
                        
        
        return max_len * max_len
        
        
                    
        