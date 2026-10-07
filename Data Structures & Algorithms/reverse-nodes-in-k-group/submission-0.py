# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            # Trouver le dernier nœud du groupe
            kth = group_prev

            for i in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            group_next = kth.next

            # Reverse du groupe
            previous = group_next
            current = group_prev.next

            while current != group_next:
                a = current.next
                current.next = previous
                previous = current
                current = a

            # Relier le groupe précédent au groupe inversé
            a = group_prev.next
            group_prev.next = kth
            group_prev = a


