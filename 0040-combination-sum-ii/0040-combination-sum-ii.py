class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        seen_combination = set()
        candidates.sort()
        
        def helper(start_idx, combination, _target):
            if _target == 0:
                res.append(combination.copy())
                return;
                    
            for i in range(start_idx, len(candidates)):
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                if -candidates[i] > _target:
                    break
                combination.append(candidates[i])
                helper(i+1, combination, _target-candidates[i])
                combination.pop()
        helper(0, [], target)
        return res