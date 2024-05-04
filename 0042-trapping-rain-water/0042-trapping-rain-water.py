class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        top_left, top_right = height[0], height[r]
        
        res = 0
        while l < r:
            if top_left <= top_right:
                res += top_left - height[l]
                l += 1
                top_left = max(top_left, height[l])
            else:
                res += top_right - height[r]
                r -= 1
                top_right = max(top_right, height[r])
        return res