"""
Problem: Container With Most Water

Summary:

* Given heights[i] representing vertical lines, choose two lines such that
  the container formed holds the maximum amount of water.
* Area is calculated as:
  area = min(height[left], height[right]) * (right - left)

Approach:

* Use two pointers starting at both ends of the array.
* At each step:

  * Compute the current area.
  * Update the maximum area found.
  * Move the pointer at the *shorter* height inward.
* Rationale:

  * The shorter line limits the height of the container.
  * Moving the taller line cannot increase area because width decreases
    and the limiting height stays the same.
  * Moving the shorter line may find a taller boundary and increase area.

Time complexity: O(n)

* Each pointer moves at most n times.

Space complexity: O(1)

* Only uses a few variables, no extra space.

Notes / what I learned:

* This is a classic two-pointer problem.
* Key pattern: “move the bottleneck”.
* Greedy choice works because we never skip a better solution by discarding
  the shorter side.
  """
class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        return result
        