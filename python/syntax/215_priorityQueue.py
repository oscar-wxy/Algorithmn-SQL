"""
python list cut will create a new list in the memory
example: a[:k] will create a new one
heapq or priorityqueue only support min heap, one way to solve this(implement max heap), is to overwrite __lt__
example is at the bottom

heapq is the implementation of PriorityQueue
heapq comparison is based on the __lt__
"""
import heapq
from queue import PriorityQueue
from typing import List

"""
min heap:
maintain the largest k elements
the root/top of the min heap is the answer
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # in place, O(x)
        # create the first k elements, new object in the memory
        heap = nums[:k]
        heapq.heapify(heap)

        for ele in nums[k:]:
            # if we want to peek, use heap[0]
            if ele > heap[0]:
                # heapq.heappush(ele)
                # heapq.heappop()
                # above two lines can be replaced by below
                heapq.heapreplace(heap, ele)

        return heap[0]

# try max heap

# wrap the number
class NumberForMaxHeap(object):
    def __init__(self,x):
        self.x = x

    def __lt__(self, other):
        return self.x > other.x

    def __str__(self):
        return str(self.x)

    def __gt__(self, other):
        return self.x < other
# test it
a = [12,4,6,7,8,1,2]
heap = []
heapq.heapify(heap)
for ele in a:
    heapq.heappush(heap,NumberForMaxHeap(ele))

# print(heapq.heappop(heap))
for x in range(len(a)):
    print(heapq.heappop(heap))

# Max Heap
class MaxHeapElement(object):

    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return self.x > other.x

    def __str__(self):
        return str(self.x)


max_heap = PriorityQueue()

max_heap.put(MaxHeapElement(10))
max_heap.put(MaxHeapElement(20))
max_heap.put(MaxHeapElement(15))
max_heap.put(MaxHeapElement(12))
max_heap.put(MaxHeapElement(27))

while not max_heap.empty():
    print(max_heap.get())
