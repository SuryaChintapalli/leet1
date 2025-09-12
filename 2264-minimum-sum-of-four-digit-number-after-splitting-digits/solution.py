class Solution:
    def minimumSum(self, num: int) -> int:
        n=str(num)
        s=sorted(n)
        n1=int(s[0]+s[2])
        n2=int(s[1]+s[3])
        return n1+n2
