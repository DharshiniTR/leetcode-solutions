class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        v=False
        c=False
        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in "AEIOUaeiou":
                    v=True
                else:
                    c=True
        return v and c
            
        