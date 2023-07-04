from collections import OrderedDict
"""
print(not 0)
b = OrderedDict()
b['fisrt'] = 1
b['second'] = 2
print(b.popitem())
print(b.popitem())
('second', 2)
('fisrt', 1)
"""
"""
总结：
python所有的dict如何避免keyerror 或者 是避免 key in dict.keys():浪费
1.dict.get(key,default=None)
2.t.setdefault('d',default=None), 相当于java的getordefault
t.setdefault('d', 'not exist')
{'c': '3', 'd': 'not exist', 'a': '1', 'b': '2'}

OrderedDict:pop方法可以pop首尾的k，v
dict.del的时间复杂度：
"""

"""
 [1,2,3,4,5,6,7,5] => within a slide window, which size of k + 1, is there any nums[i] - nums[j] <= t ?

 6:22

 start from : 
 l=0, r=0 => l =0, r=k:
    use a bucket, which the size is: 
    t = 2, f(0) = 0, f(1) = 0, f(2) = 0, f(3) = 1, the size, also the "divider" = t + 1
    [0,1,2], [3,4,5], [6,7,8]
    bucket = here we use a hashtable, to save memory, bucket = {bucket_idx:bucket_val}
    tricky part:  we need to remove and delete the key, try to know the time complexity for orderedict and dict

    when we add a new number:
    if there is already a number exist in the bucket[idx], then return True

    If there is a number exist in bucket[idx - 1], or bucjket[idx + 1], compare
        If meet the reuquirement, return true
        If not, add it in the bucket



"""

"""
First version, use a dict
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        bucket = {}
        l = 0
        r = 0

        # to make it faster, we store the idx
        for i in range(len(nums)):
            # if i is bigger than k, remove the bucket[i-k-1], [0,...k] => [1,....k+1]
            if i > k:
                del bucket[nums[i - k - 1] / (t + 1)]  # ordereddict直接pop就行
            idx = nums[i] // (t + 1)
            if bucket.get(idx) is not None:  # not sufficient, how to optimize? ordereddict会返回none
                return True
            if bucket.get(idx + 1) is not None: # funny story, if bucket.get(idx) =? false, if is not None => True
                if abs(nums[bucket[idx + 1]] - nums[i]) <= t:
                    return True
            if bucket.get(idx - 1) is not None:
                if abs(nums[bucket[idx - 1]] - nums[i]) <= t:
                    return True
            bucket[idx] = i

        return False




