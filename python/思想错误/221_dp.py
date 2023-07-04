"""
Why you are wrong?
For dp question,
DP数组靠后的永远应该based on 前面的

if map.get((row,col)) == cur and 
map.get((row,col+1)) == cur and 
map.get((row+1,col)) == cur and 
map.get((row+1,col+1)) == cur:
map[(row,col)] = cur + 1

就很离谱。往往会造成不必要的浪费

"""

"""
use dp, recur
for each round, we have a initial cur which means the square length so far
the goal for each round is to get the cur+1 for this round, then go next
use memo + recur + dp

formula:
f(i,j) = k+1 if f(i,j)=k, f(i,j+1)=K,f(I+1,j)=k, f(i+1,j+1) = k
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        map = {}
        
                    
        def search(cur):
            rows = len(matrix) - cur + 1
            cols = len(matrix[0]) - cur + 1
            increased = False
            for row in range(rows):
                for col in range(cols):
                    if map.get((row,col)) is None:
                        continue
                        
                    if map.get((row,col)) == cur and map.get((row,col+1)) == cur and map.get((row+1,col)) == cur and map.get((row+1,col+1)) == cur:
                        map[(row,col)] = cur + 1
                        increased = True
            
            return search(cur+1) if increased else cur
        
        # now initialize the map
        all_zero = True
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    map[(row,col)]=1
                    all_zero = False
        
        if all_zero:
            return 0
        
        max_len =  search(1)
        return max_len*max_len
        
        