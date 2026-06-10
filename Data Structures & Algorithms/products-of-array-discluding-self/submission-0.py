class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1]*len(nums)
        left  = [1]*len(nums)

        r = l = 1

        for i in range(len(nums)):
            left[i]=l
            l *= nums[i]
            i+=1


        for j in range(len(nums)-1,-1,-1):
            right[j] =r
            r*= nums[j]
            j-=1
        
        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i]=left[i]*right[i]

        return res