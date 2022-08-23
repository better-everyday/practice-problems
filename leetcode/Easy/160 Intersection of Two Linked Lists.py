"""
--- Description ---

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        # 1.
        """
        def traverse(head, list):
            if head:
                list.append(head.val)
                traverse(head.next, list)

        listA = []
        listB = []
        traverse(headA, listA)
        traverse(headB, listB)

        listA = listA[::-1]
        listB = listB[::-1]

        skip = 0
        for i, n in enumerate(listA):
            try:
                if n == listB[i]:
                    skip = i+1
            except:
                break

        if skip:
            intA = "headA"
            intB = "headB"

            for x in range(len(listA)-skip):
                intA += ".next"
            for x in range(len(listB)-skip):
                intB += ".next"
            
            for x in range(skip):
                if eval(intA) == eval(intB): return eval(intA)
                else:
                    intA += ".next"
                    intB += ".next"
        """

        # 2.
        def traverse(head):
            l = 0
            while head:
                l += 1
                head = head.next
            return l

        lA, lB = traverse(headA), traverse(headB)

        skip = abs(lB-lA)
        
        if lB > lA:
            for x in range(skip):
                headB = headB.next
        else:
            for x in range(skip):
                headA = headA.next
            
        for x in range(lA):
            if headA == headB: return headA
            else:
                headA = headA.next
                headB = headB.next

"""
--- Submission ---

1.
Runtime: 193 ms, faster than 76.41% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 39.5 MB, less than 6.13% of Python3 online submissions for Intersection of Two Linked Lists.

2.
Runtime: 168 ms, faster than 90.67% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.6 MB, less than 69.73% of Python3 online submissions for Intersection of Two Linked Lists.
"""