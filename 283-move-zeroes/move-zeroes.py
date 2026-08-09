class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastpos=0
        for num in range(len(nums)):
            if nums[num]!=0:
                temp=nums[num]
                nums[num]=nums[lastpos]
                nums[lastpos]=temp
                lastpos+=1
            
            
            
        
            
        
        

        
        