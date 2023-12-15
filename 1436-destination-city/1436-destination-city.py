class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = [paths[_][0] for _ in range(len(paths))]
        dests = [paths[_][1] for _ in range(len(paths))]
        for i in range(len(paths)):
            if dests[i] not in starts:
                return dests[i]
        return None