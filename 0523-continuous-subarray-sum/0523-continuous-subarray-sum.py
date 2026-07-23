class Solution:
    def checkSubarraySum(self, arr: List[int], k: int) -> bool:
        d={0:-1}
        s=0
        for i in range(len(arr)):
            s+=arr[i]
            r=s%k
            if r in d:
                if i-d[r]>=2:
                    return True
                    break
            else:
                d[r]=i
        else:
            return False

        