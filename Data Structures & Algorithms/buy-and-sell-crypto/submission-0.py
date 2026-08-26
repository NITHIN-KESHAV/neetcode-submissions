class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        B = 0
        
        
        for S in range(B+1, len(prices)):
            if prices[B] > prices[S]:
                B = S
            curr_profit = prices[S] - prices[B]
            profit = max(profit, curr_profit)
        return profit