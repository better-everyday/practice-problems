// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1531156549
class Solution {
    public int maxProfit(int[] prices) {

        if (prices.length < 2) { return 0; }

        // sliding window for greedy solution
        int max = -99999999;
        int l, r;
        l = 0;
        r = 1;
        do {
            max = Math.max(max, Math.max(0, prices[r] - prices[l]));
            if (prices[r] < prices[l]) {
                l = r;
            }
            r++;
        } while (r <= prices.length - 1);
        return max;
    }
}