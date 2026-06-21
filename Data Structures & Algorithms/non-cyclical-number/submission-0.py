class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n!=1:
            temp = 0
            if n in visited:
                return False
            visited.add(n)
            while n:
                x = n % 10
                n //=10
                temp += x**2
            n = temp
        return True

