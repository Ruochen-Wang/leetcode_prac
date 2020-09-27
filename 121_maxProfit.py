from typing import List

def maxProfit( prices: List[int]) -> int:
    if len(prices)==0:
        return 0
    max, min = prices[0], prices[0]
    profit = 0
    for p in prices:
        if p > max:
            max = p
            profit = (max-min) if ((max-min)>profit) else profit
        if p < min:
            min = p
            max = p
    return profit

if __name__=="__main__":
    prices = [1, 7, 0, 5, 0]
    print(maxProfit(prices))
