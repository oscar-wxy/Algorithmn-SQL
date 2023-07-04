"""
classical python dfs
Learn how to sprcify type in the method header
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        current = []
        self.dfs(start=0, current=current, size=k, arr=list(range(1, n+1, 1)), res = res)
        return res
    def dfs(self, start:int, current:List[int], size:int, arr:List[int], res:List[List[int]]):
        if len(current) == size:
            # have to new a obj, otherwise all the final results are the same
            res.append(list(current))
            return
        elif start >= len(arr):
            return
        else:
            for i in range(start, len(arr), 1):
                current.append(arr[i])
                self.dfs(i + 1, current, size, arr, res)
                # back track
                current.remove(arr[i])