
# Minimum Number of Operations to Make Array Continuous

## Problem Statement

You are given an integer array `nums`. In one operation, you can replace any element in `nums` with any integer.

`nums` is considered continuous if both of the following conditions are fulfilled:
1. All elements in `nums` are unique.
2. The difference between the maximum element and the minimum element in `nums` equals `nums.length - 1`.

For example, `nums = [4, 2, 5, 3]` is continuous, but `nums = [1, 2, 3, 5, 6]` is not continuous.

Return the minimum number of operations to make `nums` continuous.

### Examples

#### Example 1:
Input: `nums = [4, 2, 5, 3]`  
Output: `0`  
Explanation: `nums` is already continuous.

#### Example 2:
Input: `nums = [1, 2, 3, 5, 6]`  
Output: `1`  
Explanation: One possible solution is to change the last element to 4.  
The resulting array is `[1, 2, 3, 5, 4]`, which is continuous.

#### Example 3:
Input: `nums = [1, 10, 100, 1000]`  
Output: `3`  
Explanation: One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is `[1, 2, 3, 4]`, which is continuous.

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Solution

### Approach

1. Convert the array `nums` into a set to remove duplicates and sort it.
2. Use two pointers, `i` and `j`, to find the minimum operations required.
3. Iterate through the array to determine the minimum number of operations to make the array continuous.

### Complexity Analysis

- **Time Complexity:** O(n log n) due to the sorting step.
- **Space Complexity:** O(n) for storing the unique elements.

### Implementation

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i, j, n0 = 0, 0, len(nums)
        nums = list(set(nums))
        nums = sorted(nums)
        n = len(nums)
        mino = n0
        while j <= n:
            if j == n or nums[j] >= nums[i] + n0:
                ops = n0 - (j-i)
                mino = min(ops, mino)
                i += 1
                if j == n:
                    break;
            else:
                j += 1
        return mino
```

### Usage

To use this solution, create an instance of the `Solution` class and call the `minOperations` method with the input list `nums`.

```python
solution = Solution()
result = solution.minOperations([4, 2, 5, 3])
print(result)  # Output: 0
```

