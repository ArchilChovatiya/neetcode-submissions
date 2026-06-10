class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for s in strs:
            anag = [0]*26
            for c in s:
                anag[ord(c)-ord('a')]+=1
            key = tuple(anag)
            if key not in results:
                results[key]=[]
            results[key].append(s)
        return list(results.values())