class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = []
        res = []
        def dfs(open,close):
            if close == n:
                res.append(curr[:])
            if open < n:
                curr.append('(')
                dfs(open+1,close)
                curr.pop()
            if close < open:
                curr.append(')')
                dfs(open, close+1)
                curr.pop()
        dfs(0,0)
        print(res)
        return ["".join(r) for r in res]
