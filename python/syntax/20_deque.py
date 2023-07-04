"""
d = collections.deque()

append => appendLast
appendleft
pop => pop last, and get the value
popleft => pop first and get the value
"""
class Solution:
    def isValid(self, s: str) -> bool:
        d = collections.deque()
        
        for i in range(len(s)):
            if len(d) == 0:
                if s[i] == '{' or s[i] == '(' or s[i] == '[':
                    d.appendleft(s[i])
                else:
                    return False
            else:
                if s[i] == '{' or s[i] == '(' or s[i] == '[':
                    d.append(s[i])
                elif s[i] == '}' and d.pop() == '{':
                    pass
                elif s[i] == ')' and d.pop() == '(':
                    pass
                elif s[i] == ']' and d.pop() == '[':
                    pass
                else:
                    return False
        
        return True if len(d) == 0 else False
                