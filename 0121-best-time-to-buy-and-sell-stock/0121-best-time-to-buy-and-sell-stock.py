class Solution(object):
    def maxProfit(self, prices):

        greatest = 0
        cheapest = prices[0]

        for i in prices: 
            cheapest = min(cheapest, i)
            greatest = max(greatest, i - cheapest)

        return greatest

        # profits = []

        # for buy in prices:
        #     for sell in prices[prices.index(buy):]:
        #         profit = sell - buy
        #         if profit > 0:
        #             profits.append(sell - buy)
        
        # if len(profits) == 0:
        #     return 0
        # else:    
        #     return max(profits)

        # if len(prices) <= 1:
        #     return 0

        # buy = min(prices)
        # buyInd = prices.index(buy)

        # if min(prices) == prices[-1]:
        #     buy = min(prices[:len(prices) - 1])
        #     buyInd = prices.index(buy)

        # sell = 0
        # for i in prices[buyInd:]:
        #     if i > sell: 
        #         sell = i

        # profit = sell - buy

        # if profit > 0:
        #     return profit
        # else: 
        #     return 0
        