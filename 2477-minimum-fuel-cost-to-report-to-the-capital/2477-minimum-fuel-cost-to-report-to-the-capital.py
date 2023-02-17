class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g = [[] for _ in range(len(roads) + 1)]
        self.res = 0
        visited = {0}
        for u, v in roads:
            g[u].append(v)
            g[v].append(u)

        def search(node, prev):
            p = 1
            for v in g[node]:
                if v == prev:
                    continue
                p += search(v, node)
            if node > 0:
                self.res += int(math.ceil(p / seats))
            return p
            
        search(0, -1)
        return self.res