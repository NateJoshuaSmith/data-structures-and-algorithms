# ============================================
# Best Time to Buy and Sell Stock - Summary
# ============================================

# Problem:
# Given an array prices where prices[i] is the price on day i,
# choose one day to buy and a later day to sell to maximize profit.

# Goal:
# profit = sell - buy

# --------------------------------------------
# Core Idea:
# Treat every day as a potential SELL day.
# At each day, ask:
# "If I sell today, what is the best (lowest) price I could have bought before today?"

# --------------------------------------------
# Key Variables:
# l = index of lowest price so far (best buy day)
# r = current day (potential sell day)
# max_profit = best profit seen so far

# --------------------------------------------
# Algorithm:
# - Iterate through the array using r
# - If current price is lower than prices[l], update l (better buy)
# - Else, calculate profit = prices[r] - prices[l]
# - Update max_profit if this profit is higher

# --------------------------------------------
# Important Rules:
# 1. profit = sell - buy
#    Think: money in - money out
#
# 2. Only update l when:
#    prices[r] < prices[l]
#    (found a cheaper day to buy)
#
# 3. r always moves forward (represents time passing)
#
# 4. We check every day because the best sell day could be anywhere

# --------------------------------------------
# Time Complexity:
# O(n) → we scan the array once

# Space Complexity:
# O(1) → we use only a few variables

# --------------------------------------------
# Pattern:
# - Greedy
# - Single pass
# - Track minimum so far

# --------------------------------------------
# Mental Model:
# past (buy) -------- current day (sell)
#    l                     r
#
# Always:
# - buy at the lowest price seen so far
# - sell today
# - keep the maximum profit

# --------------------------------------------
# One-line Summary:
# Track the lowest price so far and compute profit at each day as if selling today.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit

