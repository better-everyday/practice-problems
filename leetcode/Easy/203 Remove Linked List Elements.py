"""
--- Description ---

Given the head of a linked list and an integer val, remove all the nodes of the linked list that 
has Node.val == val, and return the new head.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        def find_tail(head):
            current = head
            while current.next != None:
                current = current.next
            return current

        # Iteration
        new_head = None
        while head:
            if head.val != val:
                if new_head == None:
                    new_head = ListNode(head.val)
                else:
                    find_tail(new_head).next = ListNode(head.val)
            
            head = head.next
        return new_head

"""
--- Submission ---

1. 
Runtime: 6875 ms, faster than 5.09% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 19.4 MB, less than 9.02% of Python3 online submissions for Remove Linked List Elements.
"""