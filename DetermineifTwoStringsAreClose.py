class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        occurrence = {}
        
        occurrence2 = {}
        
        if len(word1) != len(word2):
            return False
        
        for char in word1:
            # If entry doesn't exist yet
            if occurrence.get(char) == None:
                occurrence[char] = 1
            else:
                occurrence[char] = occurrence[char] + 1
        
        for char in word2:
            # If entry doesn't exist yet
            if occurrence2.get(char) == None:
                occurrence2[char] = 1
            else:
                occurrence2[char] = occurrence2[char] + 1
        
                
        for entry in occurrence:
            for match in occurrence2:
                if occurrence.get(entry) == occurrence2.get(match):
                    occurrence2[match] = 0
                    break
        
        for entry in occurrence2:
            # Check for new chars
            if occurrence.get(entry) == None:
                return False
            
            if occurrence2[entry] != 0:
                return False
        
        return True
