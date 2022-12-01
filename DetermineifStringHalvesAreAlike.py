class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        half = len(s)/2
        a = s[:half]
        
        b = s[half:]
        
        aVowels = 0
        bVowels = 0
        
        for char in a:
            if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
                aVowels += 1
        
        for char in b:
            if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
                bVowels += 1
        
        if aVowels == bVowels:
            return True
        else:
            return False
