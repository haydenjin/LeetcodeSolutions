# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import math

class Solution:
    def firstBadVersion(self, n: int) -> int:

        if n == 1:
            if isBadVersion(1):
                return 1
            else:
                return 0

        low = 1
        high = n

        while(low < high):
            middle = math.floor((low + high) / 2)
            if isBadVersion(middle):
                high = middle
            else:
                low = middle + 1
        
        return high
