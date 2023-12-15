class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        
        for path in paths:
            d[path[0]] = path[1]
        
        dest = paths[0][1]
        while dest in d:
            dest = d[dest]
        
        return dest