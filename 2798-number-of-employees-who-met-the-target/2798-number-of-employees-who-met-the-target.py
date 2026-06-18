class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c=0
        for num in hours:
            if num>=target:
                c=c+1
        return c

        