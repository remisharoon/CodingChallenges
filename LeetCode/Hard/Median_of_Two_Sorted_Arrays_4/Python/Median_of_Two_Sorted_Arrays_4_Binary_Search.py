class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            nums1 = nums2
        if not nums2:
            nums2 = nums1
        slist, llist = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)

        print("slist, llist = ", slist, llist)
        tlen = len(slist) + len(llist)

        # finding search space in slist
        slistminelems = 0
        slistmaxelems = len(slist)

        def isMedian(slistmidelems, llistmidelems):
            if slistmidelems > 0 and slistmidelems < len(slist):
                lmax = max(slist[slistmidelems - 1], llist[llistmidelems - 1])
                rmin = min(slist[slistmidelems], llist[llistmidelems])
            elif slistmidelems == 0 and llistmidelems < len(llist):
                lmax = llist[llistmidelems - 1]
                rmin = min(slist[slistmidelems], llist[llistmidelems])
            elif slistmidelems == len(slist) and llistmidelems > 0:
                lmax = max(slist[slistmidelems - 1], llist[llistmidelems - 1])
                rmin = llist[llistmidelems]
            elif slistmidelems == 0 and llistmidelems == len(llist):
                lmax = llist[llistmidelems - 1]
                rmin = slist[0]
            elif slistmidelems == len(slist) and llistmidelems == 0:
                lmax = slist[slistmidelems - 1]
                rmin = llist[0]

            print("lmax,rmin = ", lmax, rmin)
            return (rmin, lmax)

        def prune(slistminelems, slistmaxelems):
            print("pruning...", slistminelems, slistmaxelems)
            slistmidelems = slistminelems + (slistmaxelems - slistminelems) // 2
            llistmidelems = tlen // 2 - slistmidelems
            SLeft = slist[slistmidelems - 1] if slistmidelems > 0 else float('-inf')
            Lleft = llist[llistmidelems - 1] if llistmidelems > 0 else float('-inf')

            SRight = slist[slistmidelems] if slistmidelems < len(slist) else float('inf')
            LRight = llist[llistmidelems] if llistmidelems < len(llist) else float('inf')
            print("SLeft,Lleft,SRight,LRight = ", SLeft, Lleft, SRight, LRight)
            if SLeft > LRight or SRight > Lleft:
                slistminelems, slistmaxelems = (slistminelems, (slistmidelems - 1))
            else:
                slistminelems, slistmaxelems = (slistmidelems + 1, slistmaxelems)
            return (slistminelems, slistmaxelems)

        def binSearch(slistminelems, slistmaxelems):
            print("slistminelems,slistmaxelems = ", slistminelems, slistmaxelems)
            slistmidelems = slistminelems + (slistmaxelems - slistminelems) // 2
            llistmidelems = tlen // 2 - slistmidelems
            print("llistmidelems, slistmidelems = ", llistmidelems, slistmidelems)
            rmin, lmax = isMedian(slistmidelems, llistmidelems)
            if rmin >= lmax:
                if tlen % 2 == 0:
                    return (rmin + lmax) / 2
                else:
                    return rmin
            else:
                slistminelems, slistmaxelems = prune(slistminelems, slistmaxelems)
                return binSearch(slistminelems, slistmaxelems)

        return binSearch(slistminelems, slistmaxelems)
