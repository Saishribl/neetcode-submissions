class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxending = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            v1 = maxending + nums[i]
            v2 = nums[i]
            maxending = max(v1, v2)
            res = max(res, maxending)
        return res