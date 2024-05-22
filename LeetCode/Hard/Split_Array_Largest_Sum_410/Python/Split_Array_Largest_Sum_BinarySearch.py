from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        minb, maxb = max(nums), sum(nums)

        def canSplit(lsum):
            splits, rsum = 0, 0
            for num in nums:
                rsum += num
                if rsum > lsum:
                    splits += 1
                    rsum = num
            splits += 1
            return splits <= k

        lsum = None
        lminsum = maxb
        while maxb >= minb:
            lsum = minb + ((maxb - minb) // 2)
            #print(minb, maxb, lsum)
            if canSplit(lsum):
                maxb = lsum - 1
                lminsum = min(lminsum, lsum)
            else:
                minb = lsum + 1
        return lminsum

