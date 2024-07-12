class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        cache = {}

        def dp(i, j):
            if i == l1 or j == l2:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            c1, c2 = text1[i], text2[j]
            if c1 == c2:
                cache[(i, j)] = dp(i + 1, j + 1) + 1
            else:
                cache[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))
            return cache[(i, j)]

        return dp(0, 0)
