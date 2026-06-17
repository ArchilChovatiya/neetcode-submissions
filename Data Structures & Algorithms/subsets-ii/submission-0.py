class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort the list : O(n log(n))
        nums.sort()
        res = []
        curr = []
        def dfs(index):
            if index == len(nums):
                res.append(curr[:])
                return

            curr.append(nums[index])
            dfs(index + 1)
            curr.pop()
            j = index
            while j < len(nums) and nums[index] == nums[j]:
                j+=1
            dfs(j) 
        dfs(0)
        return res

