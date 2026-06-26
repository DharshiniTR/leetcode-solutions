class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        c={}
        ans=0
        for i in range(len(fruits)):
            if fruits[i] in c:
                c[fruits[i]]+=1
            else:
                c[fruits[i]]=1
            while len(c)>2:
                c[fruits[l]]-=1
                if c[fruits[l]]==0:
                    del c[fruits[l]]
                l+=1
            ans=max(ans,i-l+1)
        return ans
        