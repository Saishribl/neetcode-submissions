class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        min_len = float('inf')
        summ = 0

        for high in range(len(nums)):
            summ+=nums[high]

            while summ >=target:
                length = high - low + 1
                min_len = min(min_len, length)

                summ-=nums[low]
                low+=1
        if min_len == float('inf'):
            return 0
        else:
            return min_len