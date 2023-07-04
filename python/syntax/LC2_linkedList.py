# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def func(self, l1, l2, add):
        if l1 == None and l2 == None:
            if add == 1:
                return ListNode(1)
            else:
                return None
        
        elif l1 == None or l2 == None:
            empty = l1 if l1 == None else l2
            non_empty = l1 if l2 == None else l2
            
            sum = non_empty.val + add
            if sum == 10:
                non_empty.val = 0
                non_empty.next = self.func(empty, non_empty.next, 1)
                return non_empty
            else:
                non_empty.val = sum
                return non_empty
        
        else:
            sum = l1.val + l2.val + add
            val = int(sum % 10)
            new_add = int(sum / 10)
            l1.val = val
            l1.next = self.func(l1.next, l2.next, new_add)
            return l1
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.func(l1, l2, 0)

"""
python 的浮点数机制让乘除加减结果不精确切小数点后很多位, 要用int(), decimal()等让它精确  
调用class内的方法要用self.method_name
"""