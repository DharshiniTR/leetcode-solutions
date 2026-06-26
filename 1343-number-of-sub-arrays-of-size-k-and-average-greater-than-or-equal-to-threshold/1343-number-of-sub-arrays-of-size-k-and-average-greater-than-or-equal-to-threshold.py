class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s=sum(arr[:k])
        a=s//k
        ans=[]
        if a>=threshold:
            ans.append(a)
        
        for i in range(k,len(arr)):
            
            s=s+arr[i]
            s=s-arr[i-k]
            if (s//k)>=threshold:
               ans.append(s//k)
        print(ans)
        return len(ans)      