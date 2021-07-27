class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        if(len(text))<7:
            return 0 
        
        
        a = text.count('a')
        b = text.count('b')
        l = text.count('l')/2
        n = text.count('n')
        o = text.count('o')/2
        
        charCount = [a,b,l,n,o]
        print(charCount)
        if(min(charCount)!=0):
            
            return min(charCount)
        else:
            return 0
            
        
        
        
            
            
        
            
                
            
            
                    
            
        