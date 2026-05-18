class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # List is small, so just calculate all possibilities and pick the largest
        if len(prices) < 2:
            return 0
        profit_loss = set()
        profit_loss.add(0)
        for buy_day, buy_price in enumerate(prices[:-1]):
            for sell_price in prices[buy_day+1:]:
                profit_loss.add(sell_price - buy_price)
        return max(profit_loss)
