class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack:
                    return False
                begin = stack[-1]
                if (begin != '(' and char == ')' )or (begin != '[' and char == ']') or (begin != '{' and char == '}'):
                    return False
                else:
                    stack.pop()

        return not stack

                
