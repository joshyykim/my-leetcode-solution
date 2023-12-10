class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        import numpy
        return list(numpy.array(matrix).T)