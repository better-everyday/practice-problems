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

        # 1. Iteration
        # def find_tail(head):
        #     current = head
        #     while current.next != None:
        #         current = current.next
        #     return current

        # new_head = None
        # while head:
        #     if head.val != val:
        #         if new_head == None:
        #             new_head = ListNode(head.val)
        #         else:
        #             find_tail(new_head).next = ListNode(head.val)
        #     head = head.next
        # return new_head

        # 2. Stitching ????
        # def find_tail(head):
        #     current = head
        #     while current.val != val:
        #         current = current.next    
        #     return current.next
        # new_head = None
        # current = head
        # while head: 
        #     head = head.next
        # return new_head

        # 2. Recursion
        # def check(head, val):
        #     if head:
        #         if head.val == val:
        #             head = check(head.next, val)
        #         else:
        #             head.next = check(head.next, val)
        #     return head
        # return check(head, val)

        # 3. Better iterative
        res = ListNode()      
        res_iter = res
        iterator = head
        while iterator:
            if iterator.val != val:
				# As long as the value of node is different than target, add list starting from this Node
                res_iter.next = iterator
                res_iter = res_iter.next
            iterator = iterator.next
			# Set res_iter.next to None, so we're adding only Node we processed
            res_iter.next = None
        return res.next

"""
--- Submission ---

1. Iteration 
Runtime: 6875 ms, faster than 5.09% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 19.4 MB, less than 9.02% of Python3 online submissions for Remove Linked List Elements.

2. Recursion
Runtime: 72 ms, faster than 92.78% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 27 MB, less than 5.56% of Python3 online submissions for Remove Linked List Elements.
"""