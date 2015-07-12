# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        pointA = headA
        pointB = headB
        
        while pointA is not pointB:
            pointA = headB if pointA is None else pointA.next
            pointB = headA if pointB is None else pointB.next # 走到结尾换个head继续走
            
        return pointA # 找到交点时退出循环 或者 都为None退出循环 

        
