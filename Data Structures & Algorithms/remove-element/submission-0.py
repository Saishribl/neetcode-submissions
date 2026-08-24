class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low = 0
        high = 0
        
        for high in range(len(nums)):
            if nums[high]!=val:
                nums[low], nums[high] = nums[high], nums[low]
                low+=1
        return low