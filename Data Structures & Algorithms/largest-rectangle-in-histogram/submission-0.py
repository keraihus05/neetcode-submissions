class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for ind, h in enumerate(heights):
            start = ind

            while stack and h < stack[-1][1]:
                prev_ind, prev_h = stack.pop()

                area = (ind - prev_ind)* prev_h
                max_area = max(area, max_area)

                start = prev_ind
            stack.append((start, h))

        for start, h in stack:
            area = (len(heights)-start)* h
            max_area = max(area, max_area)
        return max_area
        



            

        


