class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        r = l = 1

        for i in range(len(nums)):
            res[i]=l
            l *= nums[i]

        for j in range(len(nums)-1,-1,-1):
            res[j] *=r
            r*= nums[j]
        


        return res