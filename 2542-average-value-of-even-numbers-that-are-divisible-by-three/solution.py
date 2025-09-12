class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=0
        count=0
        for num in nums:
            if num%6==0:
                s=s+num
                count+=1
        if s==0:
            return 0
        else:
            return s//count
        
