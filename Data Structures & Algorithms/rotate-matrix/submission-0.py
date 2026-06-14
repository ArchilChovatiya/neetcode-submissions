class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        l = t = 0
        b = r = n - 1
        while l < r:
            for i in range(r - l):
                matrix[t + i][r], matrix[b][r - i], matrix[b-i][l], matrix[t][l + i] = matrix[t][l + i], matrix[t + i][r], matrix[b][r - i], matrix[b-i][l]
            l+=1
            r-=1
            t+=1
            b-=1