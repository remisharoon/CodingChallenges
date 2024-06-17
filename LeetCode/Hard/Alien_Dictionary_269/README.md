
# Alien Dictionary Coding Challenge

## Challenge Description
In the "Alien Dictionary" problem, you are given a list of words from an alien language, where words are sorted lexicographically by the rules of this language. Your task is to derive and return the order of characters in the alien language. It is possible that more than one valid order exists for any given test case. If it is impossible to determine the order, return an empty string.

## Function Signature
```python
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
```

## Input Format
- `words`: a list of strings where each string represents a word in the alien language.

## Output Format
- Return the order of characters in the alien language as a string. If no valid order exists, return an empty string.

## Methodology
The solution involves the following steps:
1. Construct a directed graph where each character in the alien language represents a node, and directed edges define the precedence relationships between characters.
2. Use topological sorting to determine the order of characters. This process involves:
   - Creating adjacency lists and in-degree counts for each character based on the given words.
   - Using Depth-First Search (DFS) to detect cycles and sort the characters.
   - If a cycle is detected, the order cannot be determined, and an empty string is returned.

## Usage
Instantiate the `Solution` class and call the `foreignDictionary` method with the list of alien words. Example:
```python
sol = Solution()
result = sol.foreignDictionary(["word1", "word2", "word3"])
print(result)  # Output: 'abcde'
```

## Notes
- The problem assumes that all input words are lowercase.
- If the list of words is empty or consists of a single word, the output is simply the concatenation of unique characters in the word(s).

## Resources
For more information, visit:
- [LeetCode Problem Description](https://leetcode.com/problems/alien-dictionary/description/)
- [Neetcode Explanation](https://neetcode.io/problems/foreign-dictionary)
