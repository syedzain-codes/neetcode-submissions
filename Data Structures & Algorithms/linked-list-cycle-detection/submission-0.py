# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l1 = []
        curr = head

        while curr not in l1:
            if curr == None:
                return False

            l1.append(curr)   
            curr = curr.next

        return True        

                
        