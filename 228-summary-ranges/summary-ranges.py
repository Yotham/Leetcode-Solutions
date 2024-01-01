class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []:
            return None
        begin = 0
        end = 0
        check = False
        storage = {}
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1] and not check:
                check = True
                begin = nums[i]
                end = nums[i+1]
            elif nums[i] + 1 == nums[i+1] and check:
                end = nums[i+1]
            if nums[i] + 1 != nums[i+1]:
                check = False
                if nums[i] not in storage.values():
                    storage[nums[i]] = nums[i]
                continue
            
            storage[begin] = end

        lastIncluded = False
        finalOut = []
        last = nums[len(nums)-1]
        for key,value in sorted(storage.items()):
            if key != value:
                finalOut.append("{}->{}".format(key,value))
            else:
                finalOut.append("{}".format(key))
            if last == value:
                lastIncluded = True

        if not lastIncluded:
            finalOut.append(str(last))

        return finalOut