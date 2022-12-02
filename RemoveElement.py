class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
    
        
        try:
            while nums.index(val) != None:
                nums.pop(nums.index(val))
                print(nums)
        except:
            return
