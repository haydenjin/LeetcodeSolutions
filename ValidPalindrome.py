import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        # Removes all spaces and converts to lower case
        cleanedString = s.replace(" ", "").lower()
        # Removes all punctuation 
        cleanedString = cleanedString.translate(str.maketrans('', '', string.punctuation))

        stack = []

        for char in cleanedString:
            stack.append(char)

        for char in cleanedString:
            test = stack.pop()
            if test != char:
                return False
        
        return True
