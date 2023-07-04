"""
start 12:25
which context can win:
numebr 0 - 10, first win
number 11, second win
number 12, first win
number 13,

dp:
what is the rule:

dp[i] = true means the first player at, desired total i can win

dp[i+1] = dp[i-1] & ()
dp[0] = True, remain step: desired total, so from dp[0] => dp[0+maxChoose], all true
dp[11] = false,

will use a two dimemsion dp[][],
"""

"""
Solution1, memop cash ,use hashtable to store, as table in DP
question: does it have to be exact one winner for 13
"""


class Solution(object):

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        memo = {}

        def judge(choices, remained):
            # use the tuple as hash key
            key = tuple(choices)
            if memo.get(key) is not None:
                return memo[key]

            if choices[-1] >= remained:
                memo[key] = True
                return True

            # iterate all the possibilities
            for idx in range(len(choices)):
                # was doing if not judge(choices[:idx-1]+choices[idx+1:],remained - choices[idx]):, need to be careful
                if not judge(choices[:idx] + choices[idx + 1:], remained - choices[idx]):
                    memo[key] = True
                    return True
            memo[key] = False
            return False

        sum_ = (maxChoosableInteger + 1) * maxChoosableInteger / 2
        if desiredTotal > sum_:
            return False

        if desiredTotal == sum_:
            return True if maxChoosableInteger % 2 == 1 else False

        choices = [i for i in range(1, maxChoosableInteger + 1, 1)]

        return judge(choices, desiredTotal)

print(Solution().canIWin(10,11))








