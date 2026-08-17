class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) - 1
        water_held = 0

        while low < high:
            water = min(heights[low], heights[high]) * (high - low)
            if water > water_held:
                water_held = water

            if heights[low] < heights[high]:
                low+=1
            elif heights[low] > heights[high]:
                high-=1
            else:
                high-=1
        return water_held