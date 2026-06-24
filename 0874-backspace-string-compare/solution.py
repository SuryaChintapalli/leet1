class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        for ch in s:
            if ch=='#'and len(s1)>0:
                s1.pop()               
            elif ch!='#':
                s1.append(ch)

        for ch in t:
            if ch=='#'and len(s2)>0:
                s2.pop()
            elif ch!='#':
                s2.append(ch)
                
        return s1==s2
                
        
