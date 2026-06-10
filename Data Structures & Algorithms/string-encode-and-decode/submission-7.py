class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        res = []
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res.append(str(sz)+',')
        res.append('#')

        return "".join(res + strs)

    def decode(self, s: str) -> List[str]:
        res = []
        mid = s.index('#')
        sizes = s[:mid]
        sizes = [int(size) for size in sizes.split(',') if size!=""]
        i = mid + 1
        for sz in sizes:
            res.append(s[i:i+sz])
            i+=sz
        return res



