# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        holder = 0
        finder = 0
        for finder in range(len(nums)):
            if nums[finder] != 0:
                nums[finder], nums[holder] = nums[holder], nums[finder]
                holder += 1
        
        return nums