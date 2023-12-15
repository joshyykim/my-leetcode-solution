class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest = paths[0][1]
        for i in range(1,len(paths)):
            for j in range(1,len(paths)):
                if dest == paths[j][0]:
                    dest = paths[j][1]
        return dest