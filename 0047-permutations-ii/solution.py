class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        perm=permutations(nums)
        return(list(set(perm)))
        
        
