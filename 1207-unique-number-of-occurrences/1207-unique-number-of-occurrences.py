class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq=Counter(arr)
        ans=[]
        for ch in freq:
            ans.append(freq[ch])
        a=set(ans)
        return len(a)==len(ans)

        