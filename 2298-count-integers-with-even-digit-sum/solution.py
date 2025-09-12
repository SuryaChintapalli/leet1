class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for n in range(1,num+1):
            dsum=sum(int(digit)for digit in str(n))
            if dsum%2==0:
                count+=1
        return count
        
