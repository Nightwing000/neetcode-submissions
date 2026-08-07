class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #basically find larget area made by these heights
        start = 0
        end = len(heights) -1
        ans = []
        while start < end:
            smaller = min(heights[start], heights[end])
            ans.append((end - start) * smaller)
            if smaller == heights[start]:
                start += 1
            else:
                end -=1
        return int(max(ans))
