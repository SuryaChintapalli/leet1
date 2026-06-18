class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i, j = 0, 2

        while i < j < len(nums):
            peak = nums[i+1]
            if nums[i] < peak and nums[j] < peak:
                return i + 1
            i += 1
            j += 1
        return 0 if nums[1] < nums[0] else len(nums) - 1
        
