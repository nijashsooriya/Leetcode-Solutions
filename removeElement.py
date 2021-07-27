class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        nums.sort()
        
        counter=  nums.count(val)
        index= 0
        for i in range(len(nums)):
            if(nums[i]==val):
                index= i
                break
        for i in range(counter):
            nums.pop(index)
            
        print(nums)
                