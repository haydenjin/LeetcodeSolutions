class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # Original int as string
        stack = []
        stackCopy = []
        
        xString = str(x)
        
        # Use this to compare
        compare = []
        
        for char in xString:
            stack.append(char)
            stackCopy.append(char)
            
            
        for char in xString:
            compare.append(stack.pop())
            
        falseFlag = False    
        for i in range(len(xString)):
            if stackCopy[i] != compare[i]:
                falseFlag = True
            
        if falseFlag:
            return False
        else:
            return True
            
