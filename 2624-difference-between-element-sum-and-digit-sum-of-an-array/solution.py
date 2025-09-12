class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es=0
        dsum=0
        for i in nums:
            es+=i
            dsum+=sum(int(digit)for digit in str(i))
        return es-dsum
        
        
