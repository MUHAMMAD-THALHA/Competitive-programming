#BUY AND SELL PRODUCT

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price
            
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

solution = Solution()
prices = [7, 1, 5, 3, 6, 4]

result = solution.maxProfit(prices)
print(result) 

print(solution.maxProfit([7, 6, 4, 3, 1]))  
print(solution.maxProfit([1, 2, 3, 4, 5]))  
print(solution.maxProfit([2, 1]))            



