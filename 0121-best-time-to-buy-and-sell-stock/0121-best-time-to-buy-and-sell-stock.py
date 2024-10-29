class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        m=0
        for sell in prices:
            if sell>=buy:
                m=max(m,sell-buy)
            else:
                buy=sell
        return m


