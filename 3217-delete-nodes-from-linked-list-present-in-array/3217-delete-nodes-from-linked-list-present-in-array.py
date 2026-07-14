# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        r=set(nums)
        d=ListNode(0)
        d.next=head
        c=d
        while c.next:
            if c.next.val in r:
                c.next=c.next.next
            else:
                c=c.next
        return d.next
        