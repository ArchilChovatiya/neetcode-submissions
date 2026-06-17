class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def dfs(start):
            if start == len(s):
                res.append(curr[:])
                return
            for i in range(start,len(s)):
                if self.isPalindrome(s[start:i+1]):
                    curr.append(s[start:i+1])
                    dfs(i+1)
                    curr.pop()
        dfs(0)
        return res


    def isPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s)-1
        while l < r:
            if s[l]!=s[r]:
                return False
            l += 1
            r -= 1
        return True