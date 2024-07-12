class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        tab = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
        if l1 == 0 or l2 == 0:
            return 0
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    tab[i][j] = tab[i - 1][j - 1] + 1
                else:
                    t1 = tab[i][j - 1]
                    t2 = tab[i - 1][j]
                    tab[i][j] = max(t1, t2)
        return tab[l1][l2]
