class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        low = 0
        high = 0
        window = set()

        for high in range(len(nums)):
            if nums[high] in window:
                return True
            window.add(nums[high])

            if abs(high - low) >= k:
                window.remove(nums[low])
                low+=1
        return False
