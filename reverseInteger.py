class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = 0
        
        if x<0:
            negative = 1
        
        x = abs(x)
        x = str(x)
        
        length = len(x)
        reverse = ''
        i =  length
        while i>0:
            reverse += x[i-1]
            i-=1
        if(negative ==1):
            reverse = '-' + reverse
        
        reverse = int(reverse)
        
        if( (-1)*(2**31)<=reverse<=(2**31) -1):
            return reverse
            
            
        else:
            return 0