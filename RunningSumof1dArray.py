class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        runningSum = 0

        returnArray = []

        for number in nums:
            runningSum += number
            returnArray.append(runningSum)

        return returnArray
