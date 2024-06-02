# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
from enum import Enum


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        cache = {}

        def get(idx: int) -> int:
            if idx in cache:
                return cache[idx]
            else:
                e = mountain_arr.get(idx)
                cache[idx] = e
                return e

        def peak(lb: int, rb: int):
            midi = lb + (rb - lb) // 2
            lefti, righti = midi - 1, midi + 1
            mide, lefte, righte = get(midi), get(lefti), get(righti)
            if lefte < mide and righte < mide:
                return midi
            elif lefte < righte:
                return peak(midi, rb)
            else:
                return peak(lb, midi)

        arr_len = mountain_arr.length()
        pki = peak(0, arr_len - 1)
        print("peaki, cache = ", pki, cache)

        class SortingDir(Enum):
            ASCENDING = 0
            DESCENDING = 1

        def binSearch(lb: int, rb: int, sorting: SortingDir):
            print("binSearch, lb, rb, sorting = ", lb, rb, sorting)
            midi = lb + (rb - lb) // 2
            mide = get(midi)
            if mide == target:
                return midi
            elif lb == rb:
                return -1
            elif mide < target and sorting == SortingDir.ASCENDING:
                return binSearch(midi + 1, rb, SortingDir.ASCENDING)
            elif mide > target and sorting == SortingDir.ASCENDING:
                return binSearch(lb, midi, SortingDir.ASCENDING)
            elif mide < target and sorting == SortingDir.DESCENDING:
                return binSearch(lb, midi, SortingDir.DESCENDING)
            elif mide > target and sorting == SortingDir.DESCENDING:
                return binSearch(midi + 1, rb, SortingDir.DESCENDING)

        bs1 = binSearch(0, pki, SortingDir.ASCENDING)
        bs2 = binSearch(pki, arr_len - 1, SortingDir.DESCENDING)
        print(bs1, bs2)
        if bs1 > -1:
            return bs1
        else:
            return bs2
