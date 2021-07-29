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
        if(current!=None):
            while current.next:
                current= current.next
            current.next = new_node
        else:
            self.head = new_node
            current = self.head
            
        
        return self.head 
        
    
class Solution(object):
    def getLength(self,linkedList):
        
        length = 0
        
        while linkedList.next:
            length+=1
            linkedList = linkedList.next
            
        length+=1
        
        return length
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = head
        length = self.getLength(head)
        index = length-n
        LL = LinkedList()
        
        
        counter = 0
        
        if(length==1 and n==1):
            return LL.head
        
        while dummy.next:
            if(counter!=index):
                LL.append(dummy.val)
                
            dummy = dummy.next
            counter+=1
            
        
        
        print(counter,index)
        if(index!=counter):
            LL.append(dummy.val)
        
        
        return LL.head
                
        
        
        

    