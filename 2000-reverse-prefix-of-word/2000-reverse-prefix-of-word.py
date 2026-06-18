class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind=0
        for i in range(len(word)):
            if word[i]==ch:
                ind=i
                break
        s=""
        for i in range(ind,-1,-1):
            s+=word[i]
        r=s+word[ind+1:]
        return r
        

        