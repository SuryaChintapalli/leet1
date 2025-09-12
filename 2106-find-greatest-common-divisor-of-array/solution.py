class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max1=max(nums)
        min1=min(nums)
        return math.gcd(max1,min1)
        
