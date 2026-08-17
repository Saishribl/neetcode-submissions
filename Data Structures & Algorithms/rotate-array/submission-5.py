class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        d = k % n
        low = 0
        high = n - 1

        def rev(nums, low, high):
            while low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low+=1
                high-=1
        
        rev(nums, n-d, n-1)
        rev(nums,0, n-d-1)
        rev(nums, 0, n-1)
        