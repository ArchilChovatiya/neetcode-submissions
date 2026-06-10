class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l , r = 0 , len(s)-1
        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l+=1
            while l < r and not self.isAlphaNum(s[r]):
                r-=1
            if s[l]!= s[r]: return False
            l+=1
            r-=1
        return True
    
    def isAlphaNum(self, c):
        return (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('0') and ord(c) <= ord('9'))