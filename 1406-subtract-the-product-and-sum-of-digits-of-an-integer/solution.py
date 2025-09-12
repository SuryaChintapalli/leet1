class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        s=0
        for d in str(n):
            p=p*int(d)
            s=s+int(d)
        return p-s
