# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dummy = root 
        array = []
        stack = []
        length = 0
        
        if(dummy == None):
            return array 
        
        while (dummy!=None or len(stack)!=0):
            while dummy:
                stack.append(dummy)
                length+=1
                dummy = dummy.left
            
            dummy = stack.pop()
            array.append(dummy.val)
            dummy = dummy.right
            
        return array
        
        
            
        
        