class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res =  -sys.maxsize
        maxP =  1
        minP =  1

        for n in nums:
            if n == 0:
                maxP = -sys.maxsize
                minP =  sys.maxsize  
            maxP , minP = max(n * maxP, n * minP, n), min(n * maxP, n * minP, n)
            res = max(res, maxP)
        return res




