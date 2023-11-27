class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack \
                 or (char == ')' and stack[-1] != "(") or \
                 (char == '}' and stack[-1] != "{") or \
                 (char == "]" and stack[-1] != "["):
                    return False
                else:
                    stack.pop()

        return not stack

                
