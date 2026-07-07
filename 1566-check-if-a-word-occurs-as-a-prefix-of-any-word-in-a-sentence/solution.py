class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        List1=sentence.split()
        l=len(searchWord)
        for i in range(len(List1)):
            name1=str(List1[i])
            if len(List1[i])>=len(searchWord) and name1[:l]==searchWord:
                return i+1
        return -1
    
        
