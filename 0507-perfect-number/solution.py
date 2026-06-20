class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        count=1
        if num==1:
            return False
        a = int(num**0.5)
        for i in range(2, a + 1):
            if num % i == 0:
                count+=i
                if num//i != i:
                    count+=num//i
        return num==count
        
