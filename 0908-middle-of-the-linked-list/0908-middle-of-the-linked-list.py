# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h=head
        k=head
        c=0
        while(k):
            c=c+1
            k=k.next
        if(c%2==0):
            c=int(c/2)
        else:
            c=int(c/2)
        k1=0
        while(k1!=c):
            k1=k1+1
            
            if(k1==c):
                return h.next
            h=h.next
        return h

        