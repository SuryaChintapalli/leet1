class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n=[]
        for symbol in operations:
            if symbol=="+":
                n.append(n[-1]+n[-2])
            elif symbol=="D":
                n.append(n[-1]*2)
            elif symbol=="C":
                n.pop()
            else:
                n.append(int(symbol))
        return sum(n)
        
