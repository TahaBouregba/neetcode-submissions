# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []

        for  i in lists : 
            while  i :
                values.append(i.val)
                i = i.next
        
        dummy = ListNode()
        current = dummy

        values.sort()

        for  i in values : 
            current.next = ListNode(i)
            current=current.next
        return dummy.next



                
