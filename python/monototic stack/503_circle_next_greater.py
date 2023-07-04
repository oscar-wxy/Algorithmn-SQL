class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        first step:
        the same as the before, get the "right" one first. [big -> small]
        """

        stack = []
        res = [-1] * len(nums)

        for idx in range(len(nums)):
            if len(stack) == 0:
                stack.append([idx])
            # if there is already number, see if it's bigger, equal, or snmaller
            else:
                # smaller than top, then create a bew
                if nums[idx] < nums[stack[-1][0]]:
                    stack.append([idx])

                else:
                    # if it's bigger, keep popping till it's bigger or equal
                    while len(stack) > 0 and nums[idx] > nums[stack[-1][0]]:
                        # pop
                        for popped in stack.pop():
                            res[popped] = nums[idx]
                    # if it's equal, append to the exist
                    if len(stack) > 0 and nums[idx] == nums[stack[-1][0]]:
                        stack[-1].append(idx)
                    else:
                        # here was missing for the first time, pay attention to it
                        stack.append([idx])

        # for the rest sitting in the array [6,5] => [7.....6,5]
        for ele in nums:
            while len(stack) > 0 and ele > nums[stack[-1][0]]:
                for popped in stack.pop():
                    res[popped] = ele

        return res

"""
another solution on discussion
It doesn't use stack to store the list of the idx, because in this casem only need the number on the "right",
if will include the number on the left, then cannot use this way
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        res = [-1 for val in range(len(nums))]
        for i in range(len(nums)):
            while len(st) > 0 and nums[i] > nums[st[-1]]:
                cur = st.pop()
                res[cur] = nums[i]
            st.append(i)
        for i in range(len(nums)):
            while len(st) > 0 and nums[i] > nums[st[-1]]:
                cur = st.pop()
                res[cur] = nums[i]
        return res
"""