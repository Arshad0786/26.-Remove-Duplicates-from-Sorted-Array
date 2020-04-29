class Solution:
    def removeDuplicates(self, nums):
        NewArrayIndex = 0
        OldArrayIndex = 0
        if(len(nums) < 2):
            return len(nums)
        for OldArrayIndex in range(len(nums)-1):
            if(nums[OldArrayIndex] != nums[OldArrayIndex + 1]):
                nums[NewArrayIndex] = nums[OldArrayIndex]
                NewArrayIndex = NewArrayIndex + 1
        nums[NewArrayIndex] = nums[OldArrayIndex + 1]
        return NewArrayIndex + 1
