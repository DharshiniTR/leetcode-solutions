class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for ch in t:
            if ch not in s:
                return ch
            if ch in s:
                if t.count(ch)>s.count(ch):
                    return (t.count(ch)-s.count(ch))*ch
           
        
                
        