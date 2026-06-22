class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def helper(i , open):
            if (i, open) in memo:
                return memo[(i, open)]
            if open < 0:
                return False
            if i == len(s):
                return open == 0
            if s[i] == '(':
                memo[(i, open)] = helper(i+1, open + 1)
                return memo[(i, open)]
            elif s[i] ==')':
                memo[(i, open)] = helper(i+1, open - 1)
                return memo[(i, open)]
            else:
                memo[(i, open)] =  helper(i+1, open + 1) or helper(i+1, open - 1) or helper(i+1, open)
                return memo[(i, open)]
        return helper(0,0)
