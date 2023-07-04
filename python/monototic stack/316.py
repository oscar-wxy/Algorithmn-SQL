"""
python char mibus:
ord() => return ascii
example: ord('a') - ord('b') = -1
"""


class Solution(object):
    def removeDuplicateLetters(self, s):

        """
        use monotonic stack [small -> big]
        when we cannot pop? the letter is the last one 
        
        
        """
        count = {}
        answer = ""
        # build a count map
        for i in range(len(s)):
            letter = s[i]
            if letter in count.keys():
                count[letter] = count[letter] + 1
            else:
                count[letter] = 1

        # monotonic
        stack = []  # [small -> big]

        # how does python comapre letter
        for i in range(len(s)):
            letter = s[i]

            if len(stack) == 0:
                stack.append(s[i])
                # count[letter] = count[letter] - 1
            else:
                # skip if already exist
                if s[i] in stack:
                    count[s[i]] = count[s[i]] - 1
                    continue
                # pop out
                while len(stack) > 0 and s[i] < stack[-1] and count[stack[-1]] > 1:
                    count[stack[-1]] = count[stack[-1]] - 1
                    stack.pop()

                stack.append(s[i])

                # count[s[i]] = count[s[i]] - 1

        return "".join(stack)

