class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 2:
            return [0,1]
        
        for i in range(len(nums)): 
            diff = target - nums[i]
            
            location = None
            try:
                location = nums.index(diff, i + 1)
            except:
                location = None
            
            if (location):
                return [i, location]
