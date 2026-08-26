class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxending = nums[0]
        minending = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = maxending * nums[i]
            v3 = minending * nums[i]
            maxending = max(v1, v2, v3)
            minending = min(v1, v2, v3)
            res = max(res, maxending, minending)
        return res