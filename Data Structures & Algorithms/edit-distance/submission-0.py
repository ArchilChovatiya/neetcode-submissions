class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def helper(i , j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i ==len(word1):
                return len(word2) - j
            if j ==len(word2):
                return len(word1) - i 
            if word1[i] == word2[j]:
                return helper(i+1,j+1)
            insert =  helper(i  , j+1 )
            delete =  helper(i+1, j   )
            replace = helper(i+1, j+1 )
            memo[(i,j)] = min(insert, delete,replace) + 1
            return memo[(i,j)]
        return helper(0,0)