class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s=blocks[:k]
        c=0
        for ch in s:
            if ch=="W":
                c+=1
        
        mx=c
        
        for i in range(k,len(blocks)):
            if blocks[i-k]=="W":
                c-=1
            if blocks[i]=="W":
                c+=1
           
            mx=min(c,mx)
        return mx
        