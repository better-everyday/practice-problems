// https://leetcode.com/problems/binary-search/submissions/1532769383
class Solution {
    public int search(int[] nums, int target) {
        if (nums.length < 2) {
            return (nums[0] == target) ? 0 : -1;
        }

        int start, end;
        start = 0;
        end = nums.length - 1;

        while (start <= end) {
            int mid = (start + end) / 2;
            if (nums[mid] > target) {
                end = mid - 1;
            } else if (nums[mid] < target) {
                start = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}