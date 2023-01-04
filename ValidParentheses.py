class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for item in s:
            if item == '{' or item == '[' or item == '(':
                stack.append(item)
            if item == '}':
                if '{' in stack:
                    if stack.pop() != '{':
                        return False
                else:
                    return False
            if item == ']':
                if '[' in stack:
                    if stack.pop() != '[':
                        return False
                else:
                    return False
            if item == ')':
                if '(' in stack:
                    if stack.pop() != '(':
                        return False
                else:
                    return False
            
        if stack == []:
            return True
