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
            while isNum:
                length+=s[i]
                i+=1
                if s[i]=="%":
                    isNum = False
                    i+=1
            length = int(length)

            result.append(s[i:i+length])
            i=i+length
            length=""
            isNum =True
        return result



