# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math
class Solution(object):
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if(headA == headB):
            return headA
        
        dum1 = headA
        dum2 = headB    
        listA = []
        
        while dum1.next:
            listA.append(id(dum1))
            dum1 = dum1.next
            
        listA.append(id(dum1))
        
        while dum2.next:
            if(id(dum2) in listA):
                return dum2
            
            dum2 = dum2.next
        if(id(dum2) in listA):
            return dum2
            
        
        
            
        
        