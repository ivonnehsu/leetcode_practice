'''84.柱状图中最大的矩形

'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = [0] + heights + [0]
        stack = []
        result = 0
        for i in range(len(heights)):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i]<heights[stack[-1]]:
                    h = stack.pop()
                    result = max(heights[h] * (i-stack[-1]-1),result)
                stack.append(i)
        return result