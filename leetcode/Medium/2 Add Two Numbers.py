# type:ignore
"""
--- Description ---

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
- len(l1) != len(l2)
"""

# Post-Traversal
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def traverse(root, list):
            current = root
            list.append(current.val)
            if current.next != None:
                traverse(current.next, list)
        
        def add(root, num):
            if root == None:
                root = ListNode(num)
            else:
                current = root
                while current.next != None:
                    current = current.next
                current.next = ListNode(num)
        
        list1 = []
        list2 = []

        traverse(l1, list1)
        traverse(l2, list2)

        list1 = "".join([str(i) for i in list1[::-1]])
        list2 = "".join([str(i) for i in list2[::-1]])

        sum = str(int(list1) + int(list2))[::-1]
        
        root = ListNode(sum[0])
        for i in range(1, len(sum)):
            add(root, sum[i])
            
        return root

"""
--- Submission ---

Runtime: 83 ms, faster than 77.65% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.1 MB, less than 10.24% of Python3 online submissions for Add Two Numbers.
"""