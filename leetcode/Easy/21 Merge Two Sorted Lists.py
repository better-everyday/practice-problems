"""
--- Description ---

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Post-Traversal
# class Solution:
#     def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

#         def traverse(root, list):
#             current = root
#             list.append(current.val)
#             if current.next != None:
#                 traverse(current.next, list)

#         def add(root, num):
#             if root == None:
#                 root = ListNode(num)
#             else:
#                 current = root
#                 while current.next != None:
#                     current = current.next
#                 current.next = ListNode(num)

#         l1 = []
#         l2 = []

#         if list1:
#             traverse(list1, l1)
#         if list2:
#             traverse(list2, l2)

#         sorted_list = sorted(l1 + l2)

#         if sorted_list:    
#             root = ListNode(sorted_list[0])
#             for i in range(1, len(sorted_list)):
#                 add(root, sorted_list[i])
            
#             return root
        
#         return None


# In-Traversal
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        def add(root, num):
            if root == None:
                root = ListNode(num)
            else:
                current = root
                while current.next != None:
                    current = current.next
                current.next = ListNode(num)

        if not list1 and not list2:
            return None
        elif not list1:
            merged = ListNode(list2.val)
            list2 = list2.next
        elif not list2:
            merged = ListNode(list1.val)
            list1 = list1.next
        else:
            merged = ListNode(min(list1.val, list2.val))
            if list1.val < list2.val:
                list1 = list1.next
            else:
                list2 = list2.next

        while list1 != None or list2 != None:

            if list1 and list2:
                add(merged, min(list1.val, list2.val))
            elif list1 == None:
                add(merged, list2.val)
                list2 = list2.next
                continue
            else:
                add(merged, list1.val)
                list1 = list1.next
                continue
            
            if list1.val < list2.val:
                list1 = list1.next
            else:
                list2 = list2.next

        return merged

# obj = Solution()
# traverse(obj.mergeTwoLists(None,
#                            None))

"""
--- Submission ---

1. Post-Traversal
Runtime: 43 ms, faster than 85.17% of Python3 online submissions for Merge Two Sorted Lists.    O(n)
Memory Usage: 14 MB, less than 32.66% of Python3 online submissions for Merge Two Sorted Lists. O(1)

2. In-Traversal
Runtime: 43 ms, faster than 85.17% of Python3 online submissions for Merge Two Sorted Lists.        O(n)
Memory Usage: 13.9 MB, less than 32.66% of Python3 online submissions for Merge Two Sorted Lists.   O(1)
"""