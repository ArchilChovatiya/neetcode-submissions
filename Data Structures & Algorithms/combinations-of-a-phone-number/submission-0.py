class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numMap = {"2":"abc" ,"3":"def" ,"4":"ghi", "5":"jkl", "6":"mno" ,"7":"pqrs" ,"8":"tuv" ,"9":"wxyz" }
        res = []
        curr = []
        if  len(digits) == 0:
            return []
        def dfs(startI):
            if startI == len(digits):
                res.append("".join(curr))
                return
            for c in numMap[digits[startI]]:
                curr.append(c)
                dfs(startI+1)
                curr.pop()
        dfs(0)
        return res