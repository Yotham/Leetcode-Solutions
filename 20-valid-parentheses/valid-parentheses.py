class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        storage = []
        for char in s:
            if char in "{([":
                storage.append(char)
            else:
                if not storage or (char == "}" and storage[-1] != "{") or (char == "]" and storage[-1] != "[") or (char == ")" and storage[-1] != "("):
                    return False
                else:
                    storage.pop()
        return not storage