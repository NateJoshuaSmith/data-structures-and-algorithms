"""
Problem: Container With Most Water

Summary:
- Given heights[i] as vertical lines, pick two lines so that
  area = min(height[left], height[right]) * (right - left) is maximized.

Approach:
- Two pointers starting at both ends.
- At each step compute area; then move the pointer at the *shorter* line
  inward (the short side limits water; moving the tall side first cannot help).

Time complexity: O(n)
  - Each step moves left or right by one; at most n steps.

Space complexity: O(1)
  - Only a few indices and scalars; no extra data structure proportional to n.

Notes / what I learned:
- “Move the bottleneck” is a common two-pointer theme: discard the side
  that cannot improve the min height and search for a taller boundary.
- Greedy choice is safe here because we never skip the optimal pair.
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * (min(heights[l], heights[r]))
            max_area = max(max_area, area)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area