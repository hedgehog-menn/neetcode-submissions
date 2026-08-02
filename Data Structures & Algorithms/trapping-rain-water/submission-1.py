class Solution:
    def trap(self, height: List[int]) -> int:
        left_wall = right_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i - 1
            max_left[i] = left_wall
            max_right[j] = right_wall
            left_wall = max(height[i], left_wall)
            right_wall = max(height[j], right_wall)

        water = 0
        for i in range(n):
            cur_water = min(max_left[i], max_right[i]) - height[i]
            if cur_water > 0:
                water += cur_water

        return water
