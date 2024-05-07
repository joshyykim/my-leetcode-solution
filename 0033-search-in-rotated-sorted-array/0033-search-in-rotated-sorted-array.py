class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        
        while l < r:
            mid = (l + r) // 2
            # print(l, mid, r)
            if nums[l] == target:
                return l
            if nums[r-1] == target:
                return r-1
            if nums[mid] > target:
                if nums[l] > nums[mid] or nums[l] < target:
                    r = mid
                else:
                    l = mid + 1
            elif nums[mid] < target:
                if nums[mid] > nums[r-1] or nums[r-1] > target:
                    l = mid + 1
                else:
                    r = mid
            else:
                return mid
            
        return -1