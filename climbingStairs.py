
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
     
        fib = [0,1]
        i =  1
        while n>i :
        
            fib.append(fib[i]+fib[i-1])
        
            i+=1
            
        return (fib[n]+fib[n-1])