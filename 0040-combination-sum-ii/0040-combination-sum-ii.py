class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        seen_combination = set()
        candidates.sort()
        
        # if sum(candidates) < target:
        #     return res
        
        def helper(start_idx, combination):
            temp_sum = sum(combination)
            if temp_sum == target:
                res.append(combination.copy())
                return;
            elif temp_sum > target:
                return;
                    
            for i in range(start_idx, len(candidates)):
                combination.append(candidates[i])
                str_comb = ",".join([str(_) for _ in combination])
                if str_comb not in seen_combination:
                    helper(i+1, combination)
                    seen_combination.add(str_comb)
                combination.pop(-1)
        helper(0, [])
        return res