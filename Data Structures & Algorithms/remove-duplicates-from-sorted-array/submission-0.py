class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 1
        i = 0
        j = 1

        while i < j and j < len(nums):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
                unique+=1
            j+=1
        return unique