//https://leetcode.com/problems/climbing-stairs/submissions/1533900802
import java.util.Map;
import java.util.HashMap;

class Solution {
    public void recurse(Map<Integer, Integer> memo, int n) {
        if (memo.containsKey(n)) {
            return;
        }
        else {
            recurse(memo, n-2);
            recurse(memo, n-1);
            memo.put(n, Integer.sum(memo.get(n-2), memo.get(n-1)));
        }
    }

    public int climbStairs(int n) {
        // Map<Integer, Integer> memo = new HashMap<Integer, Integer>();
        // memo.put(1, 1);
        // memo.put(2, 2);

        // Recursion with Memoization
        // recurse(memo, n);

        // DP with Tabulation
        // for (int i = 3; i <= n; i++) {
        //     memo.put(i, memo.get(i-1) + memo.get(i-2));
        // }

        // DP with two pointers
        int minus_1 = 2;
        int minus_2 = 1;
        if (n == 1) 
            return minus_2;
        for (int i = 3; i <= n; i++) {
            int temp = minus_1;
            minus_1 += minus_2;
            minus_2 = temp;
        }

        return minus_1;
    }
}