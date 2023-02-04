class Solution:
    def climbStairs(self, n: int) -> int:

        if n >= 0 and n <= 2:
            return n

        oneBefore = 2
        twoBefore = 1
        
        for i in range(3,n + 1):
            if i == n:
                return (oneBefore + twoBefore)
            else:
                temp = oneBefore
                oneBefore += twoBefore
                twoBefore = temp
