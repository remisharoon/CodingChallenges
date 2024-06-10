from typing import List


class Solution:
    """
    Counts the number of subarrays with exactly k distinct integers in the given list of integers.

    Parameters:
        nums (List[int]): The list of integers.
        k (int): The number of distinct integers.

    Returns:
        int: The number of subarrays with exactly k distinct integers.
    """
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        t = 0
        for i,e in enumerate(nums):
            s = set()
            s.add(e)
            for j in range(i,len(nums)):
                s.add(nums[j])
                if len(s) == k:
                    t += 1
                elif len(s) > k:
                    break
        return t