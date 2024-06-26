class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        l, r = 0, len(matrix) * len(matrix[0])

        while l < r:
            print(l,r)
            mid = (l + r) // 2
            i, j = mid // len(matrix[0]), mid % len(matrix[0])
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid

        return False