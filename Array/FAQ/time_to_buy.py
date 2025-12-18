def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price-min_price)
    return max_profit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices)) # Expected: 5
    
    prices2 = [7, 6, 4, 3, 1]
    print(maxProfit(prices2)) # Expected: 0