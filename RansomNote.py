class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if magazine == "":
            return False

        for char in ransomNote:
            found = magazine.find(char)
            if found != -1:
                magazine = magazine.replace(char, "", 1)
            else:
                return False

        return True
