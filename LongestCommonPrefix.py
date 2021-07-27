class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        output_string = ''
        index= 0
        length = len(strs[0])
        for i in range(len(strs)):
            if(len(strs[i])<length):
                length = len(strs[i])
                index=  i
        
        
        small = [0]*len(strs)
        counter = 0
        for i in range(len(strs)):
            for j in range(len(strs[index])):
                
                if(strs[i][j] == strs[index][j]):
                    counter+=1
                else:
                    break
            small[i] = counter
            counter=0 
            
        return strs[0][0:min(small)]
                    
            
        
        
            
        
        
        
                
                
        
            
                
                
        