class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        compare = set(nums)
        
        if len(compare) == len(nums):
            return False
        else:
            return True
