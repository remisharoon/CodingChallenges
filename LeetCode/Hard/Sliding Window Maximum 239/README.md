
# Sliding Window Maximum

## Problem Description

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

### Example 1:

**Input:** 
```
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
```

**Output:** 
```
[3, 3, 5, 5, 6, 7]
```

**Explanation:** 
```
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

### Example 2:

**Input:** 
```
nums = [1], k = 1
```

**Output:** 
```
[1]
```

### Constraints:
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Solution

The solution uses a deque to maintain the indices of the elements in the current window. The algorithm processes each element of the input list and maintains the maximum element in the current window using the deque.

## Implementation

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        i, j, n = 0, 0, len(nums)
        res = []
        while j < n:
            w = j-i+1

            while dq and nums[dq[-1]] <= nums[j]:
                dq.pop()

            dq.append(j)
            
            if w == k:
                res.append(nums[dq[0]])
                if dq[0] == i:
                    dq.popleft()
                i += 1
            j += 1
        return res
```
