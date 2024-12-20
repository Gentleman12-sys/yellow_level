from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        A = headA
        lenB = 0
        B = headB

        while A:
            lenA += 1
            A = A.next
            
        while B:
            lenB += 1
            B = B.next
        
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        
        while lenB > lenA:
            headB = headB.next
            lenB -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA
    
print(Solution().getIntersectionNode([4,1,8,4,5], [5,6,1,8,4,5]))