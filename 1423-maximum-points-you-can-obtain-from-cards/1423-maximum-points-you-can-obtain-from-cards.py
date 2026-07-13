class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s=sum(cardPoints[:k])
        mx=s
        for i in range(1,k+1):
            s-=cardPoints[k-i]
            s+=cardPoints[-i]
            mx=max(s,mx)
        return mx

        