class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        appearance = {}
        
        outString = ""
        
        for char in s:
            if appearance.get(char) == None:
                appearance[char] = 1
            else:
                appearance[char] = appearance[char] + 1
        
        
        # Sort by number of appearance, then cast back to list 
        appearanceInOrder = sorted(appearance.items(), key=lambda x:x[1], reverse=True)
        
        index = 0
        for item in appearanceInOrder:
            key = item[0]
            value = item[1]
            for count in range(appearanceInOrder[index][1]):
                outString += key
            
            index += 1
        
        return outString
