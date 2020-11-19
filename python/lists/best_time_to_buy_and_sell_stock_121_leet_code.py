def maxProfit(self, prices: List[int]) -> int:
    #Brute force, this is garbage, never again
    max_profit = 0
    for idx, val in enumerate(prices):
        for jdx, jal in enumerate(prices[idx + 1:]):
            profit = jal - val
            if profit > max_profit:
                max_profit = profit
    return max_profit

# time complexity O(n), space complexity O(1), only two variables generated
def maxProfit(self, prices: List[int]) -> int:
    min_price = math.inf
    max_profit = 0
    for idx, val in enumerate(prices):
        if val < min_price:
            min_price = val
        elif val - min_price > max_profit:
            max_profit = val - min_price
    return max_profit
