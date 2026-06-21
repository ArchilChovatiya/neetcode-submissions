class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [sys.maxsize] * len(nums)
        res[0] = 0
        for i in range(len(nums)):
            for j in range(i+1, i + nums[i]+1):
                if j >= len(nums): break
                res[j] = min(res[j], res[i]+1)
        return res[-1]

