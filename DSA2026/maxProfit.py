
prices = [6,7,4,2,10,4,14]

def maxProfit(prices):
    r,l = 1,0
    maxP = 0
    
    while r< len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r= r+1
    return maxP

print(maxProfit(prices))