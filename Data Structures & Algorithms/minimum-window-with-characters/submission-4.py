from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counter = Counter(t)
        window_counter = {}
        have, need = 0 , len(target_counter)
        l = r = start = end = 0
        minLength = 1000

        while r < len(s):
            window_counter[s[r]] = window_counter.get(s[r] , 0) + 1
            if s[r] in target_counter and target_counter[s[r]] == window_counter[s[r]]:
                have+=1
            while need == have:
                if r - l < minLength:
                    minLength = r - l 
                    start = l
                    end = r + 1 
                window_counter[s[l]]-=1
                if s[l] in target_counter and window_counter[s[l]] == target_counter[s[l]] - 1:
                    have-=1
                l+=1 
            r+=1
        return s[start:end]