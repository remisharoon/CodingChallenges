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
                print("cansplit- ", splits, rsum, lsum)
            return splits >= k

        lsum = None
        while maxb > minb and (maxb - minb) > 1:
            print(minb, maxb, lsum)
            lsum = minb + (maxb - minb) // 2
            if canSplit(lsum):
                maxb = lsum
            else:
                minb = lsum
        return lsum

