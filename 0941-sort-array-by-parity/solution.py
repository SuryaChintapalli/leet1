class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        s=[]
        t=[]
        for num in nums:
            if num%2==0:
                s.append(num)
            else:
                t.append(num)
        return s+t
        
