class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        ans = []

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if len(nums[i:j+1]) == 2:
                    ans.append(sum(nums[i:j+1]))

        for i in range(len(ans)):
            for j in range(i + 1, len(ans)):
                if ans[i] == ans[j]:
                    return True

        return False