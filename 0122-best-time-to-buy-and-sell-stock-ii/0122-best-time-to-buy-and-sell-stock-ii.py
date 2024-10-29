class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        buy=prices[0]
        for sell in prices:
            if sell>=buy:
                m=m+sell-buy
                buy=sell
            else:
                buy=sell
        return m

        