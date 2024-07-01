# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=[]
        r=[]
        k=head
        while(k):
            s.append(k.val)
            k=k.next
        for i in range(len(s)-1,-1,-1):
            r.append(s[i]);
        k=head
        i=0
        while(k):
            k.val=r[i]
            i=i+1
            k=k.next
        return head


        