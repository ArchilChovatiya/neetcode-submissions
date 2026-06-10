class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map_s = [0]*26
        map_t = [0]*26
        for c in s:
            map_s[ord(c)-ord('a')]+=1
        for c in t:
            map_t[ord(c)-ord('a')]+=1
        if tuple(map_s)==tuple(map_t):
            return True
        return False