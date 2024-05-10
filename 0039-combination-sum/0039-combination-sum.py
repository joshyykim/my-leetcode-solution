class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        res = []
        
        def helper(start_idx, combination):
            if sum(combination) == target:
                res.append(combination[:])
                return;
            elif sum(combination) > target:
                return;
            
            for i in range(start_idx, len(candidates)):
                combination.append(candidates[i])
                helper(i, combination)
                combination.pop(-1)
            
        helper(0, [])
        return res