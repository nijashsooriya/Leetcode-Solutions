class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        i = 0
        j = len(x)
        counter = 0
        for i in range(len(x)):
            if(x[i] == x[j-1]):
                counter+=1
                j-=1
            
        
        if(counter == len(x)):
            return True
        else:
                return False
        