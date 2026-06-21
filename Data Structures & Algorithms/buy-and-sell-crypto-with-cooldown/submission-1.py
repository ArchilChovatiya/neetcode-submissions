class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(index, buying):
            if (index, buying) in memo:
                return memo[(index, buying)]
            if index >= len(prices):
                return 0
            cooldown = dfs(index+1, buying)
            if buying:
                buy = dfs(index+1, False)
                memo[(index, buying)] = max(buy - prices[index], cooldown)
            else:
                sell = dfs(index+2, True)
                memo[(index, buying)] = max(sell + prices[index], cooldown) 
            return memo[(index, buying)]
        return dfs(0,True)
