class Solution:
    def removeDuplicates(self, nums):
        NewArrayIndex = 0
        for OldArrayIndex in range(len(nums)):
            if(nums[NewArrayIndex] != nums[OldArrayIndex]):
                NewArrayIndex = NewArrayIndex + 1
                nums[NewArrayIndex] = nums[OldArrayIndex]
        return NewArrayIndex + 1
