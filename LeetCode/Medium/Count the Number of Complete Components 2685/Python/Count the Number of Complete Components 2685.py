from collections import defaultdict


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        cc_count = defaultdict(lambda: 1)

        edges = [sorted(edge) for edge in sorted(edges)]
        print("s-edges = ", edges)

        def find(n):
            npar = n
            while npar != par[npar]:
                npar = par[npar]

            return npar

        def union(n1, n2):
            n1par = find(n1)
            n2par = find(n2)
            # print("union n1,n2,n1par,n2par,par = ",n1,n2,n1par,n2par,par)

            if n1par == n2par:
                return 0
            elif n1par < n2par:
                par[n2par] = n1par
                cc_count[n1par] += cc_count[n2par]
            else:
                par[n1par] = n2par
                cc_count[n2par] += cc_count[n1par]

            return 1

        conn_map = defaultdict(int)

        ncc = n

        for e in edges:
            n1, n2 = e[0], e[1]
            conn_map[n1] += 1
            conn_map[n2] += 1
            ncc -= union(n1, n2)

        complconns = set()
        for n in range(n):
            p = find(n)
            complconns.add(p)

        for n, c in conn_map.items():

            npar = find(n)
            # print("n,npar,c, cc_count[npar],complconns = ", n,npar,c, cc_count[npar], complconns)
            if c < cc_count[npar] - 1:
                if npar in complconns:
                    complconns.remove(npar)

        return len(complconns)

