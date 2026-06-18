class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        best = 0
        
        while l < r:
            h = min(heights[r], heights[l])
            width = r - l

            best = max(best, (width * h))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return best
        