class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indx = {}
        for i in range(len(nums)):
            if target-nums[i] in indx:
                return[indx[target-nums[i]],i]
            else:
                indx[nums[i]]=i