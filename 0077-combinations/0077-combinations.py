class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(_) for _ in combinations([_ for _ in range(1,n+1)],k)]