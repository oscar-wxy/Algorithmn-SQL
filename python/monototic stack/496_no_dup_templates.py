class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # time for pop(): O(1), only for the last
        # in general is O(n), 
        stack = []
        num_to_greater = {}
        
        # all the element push in
        for ele in nums2:
            if len(stack) == 0:
                stack.append(ele)
            else:
                # compare the top of the stack
                # [big -> small]
                top = stack[-1]
                if ele < top:
                    stack.append(ele)
                # distinct in this case
                else:
                    #[6,4,3] <=5  change to [6,5] 
                    while len(stack) > 0 and ele > stack[-1]:
                        next = stack.pop()
                        num_to_greater[next] = ele
                    
                    stack.append(ele)
        
        # anything left
        for ele in stack:
            num_to_greater[ele] = -1
        
        # construct the res
        res = []
        for ele in nums1:
            res.append(num_to_greater[ele])
        
        return res
        