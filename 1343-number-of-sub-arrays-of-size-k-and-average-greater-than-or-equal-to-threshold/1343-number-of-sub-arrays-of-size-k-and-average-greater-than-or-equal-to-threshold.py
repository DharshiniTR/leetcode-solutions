class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s=sum(arr[:k])
        mx=[]
        if (s//k)>=threshold:
            mx.append(s//k)
        for i in range(k,len(arr)):
            s-=arr[i-k]
            s+=arr[i]
            if (s//k)>=threshold:
                mx.append(s//k)
        return len(mx)
        