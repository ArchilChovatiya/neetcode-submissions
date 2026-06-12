class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        res = [0]*(n+1)
        if s[0]!="0":
             res[0] = 1
        res[-1] = 1
        for i in range(1, n):
            if s[i]!="0":
                res[i] = res[i - 1]
            if s[i-1] == "1" or (s[i-1] == "2" and s[i] in "1234560"):
                res[i]+=res[i-2]
        return res[-2]



#
#.  1 2 3 4 5 6 2 3 
#   1 2 3
#
#