/* 
--- Description ---

Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, 
return the maximum number.
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashSet;

class Solution {
    public int thirdMax(int[] nums) {
        LinkedHashSet<Integer> set = new LinkedHashSet<Integer>();
        for (int num : nums) {
            set.add(num);
        }

        ArrayList<Integer> numList = new ArrayList<>(set);
        numList.sort(Collections.reverseOrder());
        if (numList.size() < 3) {
            return numList.get(0);
        } else {
            return numList.get(2);

        }
    }
}

/* 
--- Submission ---

Runtime: 10ms, Beats 12.32% of users with Java
Memory: 42.9MB, Beats 90.3% of users with Java
 */