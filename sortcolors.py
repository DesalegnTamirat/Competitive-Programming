class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = nums.count(0)
        b = nums.count(1)
        c = nums.count(2)
        for i in range(len(nums)):
            nums.pop()
        nums.extend([0]*a)
        nums.extend([1]*b)
        nums.extend([2]*c)
