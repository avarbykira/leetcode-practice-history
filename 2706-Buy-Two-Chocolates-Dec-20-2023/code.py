# Problem Link: https://leetcode.com/problems/buy-two-chocolates

class Solution(object):
    def buyChoco(self, prices, money):
        prices.sort()                       # simple, but O(nlogn) time complexity
        if prices[0] + prices[1] > money:
            return money
        else:
            return money - prices[0] - prices[1]
        
# improve time complexity using copilot
class Solution(object):
    def buyChoco(self, prices, money):
        if len(prices) < 2:
            return money

        min1 = min2 = float('inf')
        for price in prices:                # O(n) time complexity for just searching
            if price <= min1:
                min1, min2 = price, min1
            elif price < min2:
                min2 = price

        if min1 + min2 > money:
            return money
        else:
            return money - min1 - min2