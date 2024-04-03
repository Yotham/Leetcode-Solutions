class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        storage = {}
        for string in strs:
            storage[''.join(sorted(string))] = []

        for string in strs:
            key = ''.join(sorted(string))
            if key in storage:
                storage[key].append(string)

        final = []

        for item in storage.values():
            final.append(item)

        return final
