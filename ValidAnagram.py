class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s1 = []
        s2 = []

        if len(s) != len(t):
            return False

        for charIndex in range(len(s)):
            s1.append(s[charIndex])
            s2.append(t[charIndex])
        
        s1.sort()
        s2.sort()

        for charIndex in range(len(s1)):
            if (s1[charIndex] != s2[charIndex]):
                return False

        return True
