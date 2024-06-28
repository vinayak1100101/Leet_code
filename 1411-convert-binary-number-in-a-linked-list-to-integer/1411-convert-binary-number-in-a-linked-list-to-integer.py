# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=""
        h=head
        while h:
            k=h.val
            k=str(k)
            s=s+k
            h=h.next
        print(s)
        
        k=int(s,2)
        print(k)
        return k
        