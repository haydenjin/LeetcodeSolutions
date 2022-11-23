class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        index = 0
        
        for char in s:
            if char == 'I':
                if (index + 1) < len(s):
                    if s[index + 1] == 'V' or s[index + 1] == 'X':
                        total += -1
                    else:
                        total += 1
                else:
                    total += 1
            if char == 'V':
                total += 5
            if char == 'X':
                if (index + 1) < len(s):
                    if s[index + 1] == 'L' or s[index + 1] == 'C':
                        total += -10
                    else:
                        total += 10
                else:
                    total += 10
            if char == 'L':
                total += 50
            if char == 'C':
                if (index + 1) < len(s):
                    if s[index + 1] == 'D' or s[index + 1] == 'M':
                        total += -100
                    else:
                        total += 100
                else:
                    total += 100
            if char == 'D':
                total += 500
            if char == 'M':
                total += 1000
            index += 1
            
        return total
            
