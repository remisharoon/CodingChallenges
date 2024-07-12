
# Longest Common Subsequence Solutions

## Problem Description
Given two strings `text1` and `text2`, the task is to return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

### Example 1:
- **Input:** text1 = "abcde", text2 = "ace"
- **Output:** 3
- **Explanation:** The longest common subsequence is "ace" and its length is 3.

### Example 2:
- **Input:** text1 = "abc", text2 = "abc"
- **Output:** 3
- **Explanation:** The longest common subsequence is "abc" and its length is 3.

### Example 3:
- **Input:** text1 = "abc", text2 = "def"
- **Output:** 0
- **Explanation:** There is no such common subsequence, so the result is 0.

### Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

## Solutions

### 1. Memoization (Top-Down Dynamic Programming)

```python
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
```

#### Explanation:
- The memoization approach involves using a recursive function with a cache to store intermediate results.
- The base case is when either of the indices reaches the end of the respective string, in which case the common subsequence length is 0.
- If characters match, the result is 1 plus the result of the remaining strings.
- If characters do not match, the result is the maximum of excluding either character.
- The cache is used to avoid redundant calculations, improving efficiency.

### 2. Tabulation (Bottom-Up Dynamic Programming)

```python
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
```

#### Explanation:
- The tabulation approach uses a 2D table to iteratively build up the solution.
- The table is initialized to zeros and has dimensions (l1+1) x (l2+1) to account for empty prefixes.
- The outer loops iterate over each character of the two strings.
- If characters match, the value is 1 plus the value from the previous diagonal cell.
- If characters do not match, the value is the maximum of the cell to the left and the cell above.
- The final value in the table represents the length of the longest common subsequence.

## Summary
- The memoization approach is a top-down method that uses recursion and caching.
- The tabulation approach is a bottom-up method that uses iterative table filling.
- Both methods effectively solve the problem, with the tabulation approach generally being easier to understand and implement for dynamic programming beginners.
