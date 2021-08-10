# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        
        new_node = ListNode(data)
        current = self.head
        
        if current == None:
            self.head = new_node
            
        else:
            while current.next:
                current = current.next
                
            current.next = new_node
            
        return self.head
            
    

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = head
        place = []
        while dummy:
            place.append(dummy.val)
            dummy = dummy.next
            
        counter = 0
        
        while (counter<len(place)):
            place[counter:counter+2] = reversed(place[counter:counter+2])
            counter+=2
            
        LL = LinkedList()
        
        for i in place:
            LL.append(i)
        return LL.head
        