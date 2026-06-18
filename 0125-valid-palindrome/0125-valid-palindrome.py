class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        rev=""
        for i in range(len(s)-1,-1,-1):
            rev+=s[i]
        s1=""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isalnum():
                s1+=s[i]
    
        s2=""
        for i in range(len(rev)):
            if rev[i].isalpha() or rev[i].isalnum():
                s2+=rev[i]
        return s1==s2
       
        