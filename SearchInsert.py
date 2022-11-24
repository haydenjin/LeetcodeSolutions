class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        
        for value in nums:
            if target == value:
                return index
            if value > target:
                return index
            if index >= (len(nums) - 1):
                return index + 1
            index += 1
