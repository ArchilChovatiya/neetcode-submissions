class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))+"%"+s
        return result 

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        length = ""
        isNum = True
        while i < len(s):
            while s[i]!="%":
                length+=s[i]
                i+=1
            length = int(length)
            result.append(s[i+1:i+length+1])
            i=i+length+1
            length=""
        return result



