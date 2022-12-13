class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        li = [matrix[0][:] for i in range(len(matrix))]
        for j in range(1,len(matrix)):
            for i in range(len(matrix[j])):
                if i == 0:
                    li[j][i] = min(matrix[j][i]+li[j-1][i], matrix[j][i]+li[j-1][i+1])
                elif i == len(matrix[j])-1:
                    li[j][i] = min(matrix[j][i]+li[j-1][i-1], matrix[j][i]+li[j-1][i])
                else:
                    li[j][i] = min(matrix[j][i]+li[j-1][i-1], matrix[j][i]+li[j-1][i], matrix[j][i]+li[j-1][i+1])
        return min(li[-1])