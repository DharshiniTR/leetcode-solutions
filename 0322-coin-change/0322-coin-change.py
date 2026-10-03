class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[None]*(amount+1)
        dp[0]=[]
        for i in range(1,amount+1):
            for num in coins:
                if num<=i and dp[i-num] is not None:
                    new=dp[i-num]+[num]
                    if dp[i] is None or len(new)<len(dp[i]):
                        dp[i]=new
        if dp[amount] is not None:
            return len(dp[amount])
        else:
            return -1