class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower() or word.isupper():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        for i in range(1,len(word)):
            if word[i].isupper():
                return False
                break
            
        