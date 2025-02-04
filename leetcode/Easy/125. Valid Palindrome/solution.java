//https://leetcode.com/problems/valid-palindrome/submissions/1530418109
class Solution {
    public boolean isPalindrome(String s) {

        String replace = s.replaceAll("[^a-zA-Z0-9]", "");
        replace = replace.toLowerCase();
        for (
            int start = 0, end = replace.length() - 1;
            start < end;
            start ++, end--
        ) {
            if (replace.charAt(start) != replace.charAt(end)) { 
                return false;
            }
        }

        return true;
    }
}