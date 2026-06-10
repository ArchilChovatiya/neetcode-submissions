class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indx = {}
        for i in range(len(nums)):
            n1 = nums[i]
            n2 = target - n1
            if n2 in indx:
                return[indx[n2],i]
            else:
                indx[n1]=i