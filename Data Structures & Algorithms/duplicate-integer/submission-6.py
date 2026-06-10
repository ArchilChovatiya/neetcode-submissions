class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        record = set()
        for n in nums:
            if n in record:
                return True
            else:
                record.add(n)
        return False