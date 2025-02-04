// https://leetcode.com/problems/contains-duplicate/submissions/1530403752
class Solution {
    public boolean containsDuplicate(int[] nums) {

        Set<Integer> set = new HashSet();
        for (int num : nums) {
            boolean status = set.add(num);
            if (!status) { return true; }
        } 

        return false;
    }
}