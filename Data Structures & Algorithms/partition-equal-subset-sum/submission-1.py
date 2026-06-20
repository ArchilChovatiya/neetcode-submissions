class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        target = total//2
        memo = {}
        def dfs(i, currSum):
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            if currSum == target:
                return True
            if i >= len(nums):
                return False
            memo[(i,currSum)] = dfs(i+1, currSum + nums[i]) or dfs(i+1, currSum)
            return memo[(i,currSum)]
        return dfs(0,0)
