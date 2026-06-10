class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]
            l , r = i+1 , len(nums)-1
            while l < r:
                if nums[l]+nums[r] == target:
                    res.add((nums[i], nums[r], nums[l]))
                    l+=1 ; r-=1
                elif nums[l]+nums[r] > target:
                    r-=1
                else:
                    l+=1
        return list(res)