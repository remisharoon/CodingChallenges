from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        pcl = [i for i in range(n)]

        def findP(city):
            ci = city
            while pcl[ci] != ci:
                ci = pcl[ci]
            return pcl[ci]

        def unionC(c1, c2):
            pc1, pc2 = findP(c1), findP(c2)
            if pc1 == pc2:
                return 0
            elif pc1 < pc2:
                pcl[pc2] = pc1
            else:
                pcl[pc1] = pc2
            return 1

        np = n

        for c1 in range(n):
            for c2 in range(n):
                ic = isConnected[c1][c2]
                # print("c1, c2, ic = ", c1, c2, ic)
                if ic == 1:
                    if unionC(c1, c2):
                        np -= 1
        return np


