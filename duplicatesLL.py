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
        curr = self.head
        
        if(curr!=None):
            while curr.next:
                curr=  curr.next

            curr.next = new_node
        
        else:
            self.head = new_node
            current = self.head
        
        return self.head
        
        

class Solution(object):
    
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        LL = LinkedList()
        
        if(head==None):
            return LL.head
        
        dummy = head
        values = []
        while dummy.next:
            values.append(dummy.val)
            dummy = dummy.next
        values.append(dummy.val)
        
        for i in range(len(values)-1):
            if(values[i]==values[i+1]):
                values[i] = None
        
        values2 = []
        
        for i in range(len(values)):
            if(values[i]!=None):
                values2.append(values[i])
        
        
        for i in range(len(values2)):
            x =  LL.append(values2[i])
        
        return x`