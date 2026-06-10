class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n , 0) + 1
        
        buckets = [None]*(len(nums)+1)

        for n , c in count.items():
            if buckets[c]==None:
                buckets[c] = [n]
            else:
                buckets[c].append(n)
        
        result = []
        for i in range(len(buckets)-1,-1,-1):
            if buckets[i]!=None:
                result = result + buckets[i]
            if len(result) == k:
                break
        return result


        
        