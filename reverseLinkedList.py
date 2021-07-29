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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        LL = LinkedList()
        arr = []
        if head == None:
            return LL.head
            
            
        while head.next:
            arr.append(head.val)
            head = head.next
        arr.append(head.val)

        
        i = len(arr)-1
        while i>0:
            LL.append(arr[i])
            i-=1
        
        LL.append(arr[0])
        
        return LL.head 