from collections import deque


# [1,3,1,2,0,5]
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        i, j, n = 0, 0, len(nums)
        res = []
        while j < n:
            w = j - i + 1

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





