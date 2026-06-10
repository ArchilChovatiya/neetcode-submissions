class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for i in range((len(nums)+1))]
        
        for n in nums:
            count[n] = count.get(n , 0) + 1
        
        for n , c in count.items():
            buckets[c].append(n)
        
        result = []
        for i in range(len(buckets)-1,-1,-1):
            result = result + buckets[i]
            if len(result) == k:
                break
        return result


        
        