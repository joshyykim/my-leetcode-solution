class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return sum([list(itertools.combinations(nums, _)) for _ in range(len(nums)+1)], [])