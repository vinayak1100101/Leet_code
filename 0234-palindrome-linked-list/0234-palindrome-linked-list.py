# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        k=head
        s=""
        while(k):
            s=s+str(k.val)
            k=k.next
        return s==s[::-1]

        