class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = sorted(nums)
        t = []
        for i in range(len(nums)):
            if nums[i] == target: t.append(i)
        return t
