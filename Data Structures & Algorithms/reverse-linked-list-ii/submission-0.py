# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        curr=head
      
        
        bleft=dummy
        aright=None
        if left==right:
            return head

          
        else:
            for i in range(left-1):


    
            
                bleft=bleft.next
                
        l=bleft.next
        r=l
        for i in range(right-left):

            
            
            r=r.next
        aright=r.next

        curr=l
        prev=None
        while curr!=aright and curr!=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        bleft.next=prev
        l.next=aright
        
        
        return dummy.next
    
        

               