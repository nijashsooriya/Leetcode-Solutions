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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        root1 = l1
        root2 = l2
        arr1 = []
        arr2 = []
        
        while root1:
            arr1.append(root1.val)
            root1 = root1.next
        
        while root2:
            arr2.append(root2.val)
            root2 = root2.next
        
        
        string1 = ''
        string2= ''
        #Reverse the integers
        i = len(arr1)
        j = len(arr2)
        while i>0:
            string1 += str(arr1[i-1])
            i-=1
        while j>0:
            string2 += str(arr2[j-1])
            j-=1
        
        
        
        summation = str(int(string1)+int(string2))
        
        output_arr = []
        
        i = len(summation)
        
        while i>0:
            output_arr.append(int(summation[i-1]))
            i-=1
            
        LL = LinkedList()
        
        for i in range(len(output_arr)):
             x = LL.append(output_arr[i])
            
        return x 
            
        
    
            
        