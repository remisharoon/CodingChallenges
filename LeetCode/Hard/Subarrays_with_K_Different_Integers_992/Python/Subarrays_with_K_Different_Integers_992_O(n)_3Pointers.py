from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # [1,2,1,3,4], [1,2,1,2,3]
        t, lfp, lnp, rp, n = 0, 0, 0, 0, len(nums)
        nfreq = defaultdict(lambda: 0)
        for rp in range(n):
            re = nums[rp]
            nfreq[re] += 1

            # update LFP
            while len(nfreq) > k:
                le = nums[lnp]
                nfreq[le] -= 1
                if nfreq[le] == 0:
                    nfreq.pop(le)
                lnp += 1
                lfp = lnp
            # print("rp, lfp, lnp = ", rp, lfp, lnp)

            # Update LNP
            while len(nfreq) == k and nfreq[nums[lnp]] > 1:
                nfreq[nums[lnp]] -= 1
                lnp += 1

            if len(nfreq) == k:
                t += (lnp - lfp + 1)
                # print("t=",t)

        return t