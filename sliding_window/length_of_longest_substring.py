# Problem: Find the length of the longest substring without repeating characters
#
# Approach (Sliding Window):
# - Use two pointers (l and r) to maintain a window of unique characters
# - Use a set to track characters currently in the window
# - Expand the window by moving r forward
# - If a duplicate is found, shrink the window from the left (move l)
#   and remove characters until the duplicate is gone
# - After fixing, add the current character and update the max length
#
# Time Complexity: O(n)
# - Each character is added and removed from the set at most once
#
# Space Complexity: O(n)
# - The set can store up to n unique characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        duplicate_char = set()
        l, r = 0, 1

        for r in range(len(s)):
            while s[r] in duplicate_char:
                duplicate_char.remove(s[l])
                l += 1
            duplicate_char.add(s[r])

            length = max(length, r - l + 1)     
        return length  
