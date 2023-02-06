class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}

        longest = 0
        hasSingle = False
        totalOdd = 0

        for char in s:
            if char in dic.keys():
                dic[char] = dic[char] + 1
            else:
                dic.update({char:1})

        for key in dic:
            # If even add to count
            if dic[key] % 2 == 0:
                longest += dic[key]
            # If odd and greater than 1, add to count (but also increment totalOdd)
            else:
                if dic[key] > 1:
                    totalOdd += 1
                    longest += dic[key]
                else:
                    hasSingle = True

        if hasSingle:
            if totalOdd > 0:
                return (longest - totalOdd + 1)
            else:
                return (longest - totalOdd + 1)
        else:
            if totalOdd > 0:
                return (longest - totalOdd + 1)
            else:
                return longest
