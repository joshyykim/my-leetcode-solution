class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx = 1
        while idx < len(numbers):
            l, m, r = 0, idx // 2, idx
            while True:
                if numbers[m] + numbers[idx] == target:
                    return [m+1, idx+1]
                else:
                    if m == l or m == r:
                        break
                        
                if numbers[m] + numbers[idx] > target:
                    r = m
                    m = (l+r) // 2
                else:
                    l = m
                    m = (l+r) // 2
            idx += 1