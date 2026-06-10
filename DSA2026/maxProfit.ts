const prices: number[] = [7, 1, 5, 3, 6, 4];

function maxProfit(prices: number[]): number {
  let l = 0;
  let r = 1;
  let maxP = 0;

  while (r < prices.length) {
    if (prices[l] < prices[r]) {
      let profit = prices[r] - prices[l];

      maxP = Math.max(profit, maxP);
    } else {
      l = r;
    }
    r++;
  }
  return maxP;
}

console.log(maxProfit(prices));
