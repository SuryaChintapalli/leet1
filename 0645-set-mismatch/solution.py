from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))
        expected_sum = sum(range(1, len(nums) + 1))
        
        duplicate = actual_sum - unique_sum
        missing = expected_sum - unique_sum
        
        return [duplicate, missing]

        
