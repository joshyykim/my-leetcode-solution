class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        seen_combination = set()
        
        if sum(candidates) < target:
            return res
        
        def helper(start_idx, combination):
            list_combination = [int(_) for _ in combination.split(",") if _ != ""]
            list_combination.sort()
            temp_sum = sum(list_combination)
            if temp_sum == target and list_combination not in res:
                res.append(list_combination)
                return;
            elif temp_sum > target:
                return;
                    
            for i in range(start_idx, len(candidates)):
                if combination == "":
                    combination = str(candidates[i])
                else:
                    combination += "," + str(candidates[i])
                if combination not in seen_combination:
                    helper(i+1, combination)
                    seen_combination.add(combination)
                combination = combination[:-(1+len(str(candidates[i])))]
        
        helper(0, "")
        return res