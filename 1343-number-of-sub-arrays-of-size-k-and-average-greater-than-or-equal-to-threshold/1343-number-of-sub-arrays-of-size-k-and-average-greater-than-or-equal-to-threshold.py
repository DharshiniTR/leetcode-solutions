class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s=sum(arr[:k])
        a=s//k
        c=0
        if a>=threshold:
            c+=1
        for i in range(k,len(arr)):
            s=s-arr[i-k]+arr[i]
            a=s//k
            if a>=threshold:
                c+=1
        return c

        