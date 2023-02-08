class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dic = {}
        largest = 0
 
        for item in nums:
            if item in dic:
                dic.update({item: (dic[item] + 1)})
            else:
                dic.update({item: 1})

            if largest in dic:
                if dic[item] > dic[largest]:
                    largest = item
            else:
                largest = item

        return largest
