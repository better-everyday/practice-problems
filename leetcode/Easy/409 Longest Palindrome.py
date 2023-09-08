"""
--- Description ---

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that 
can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""

class Solution {
    public int longestPalindrome(String s) {
        Map<String, Integer> map = new HashMap<String, Integer>();
        Integer count = 0;
        Integer biggestOdd = 0;

        for  (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            map.merge(Character.toString(c), 1, Integer::sum);
        }

        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if ((entry.getValue() & 1) == 0) {
                count += entry.getValue();
            } else {
                if (entry.getValue() < biggestOdd){
                    count += entry.getValue() - 1;
                } else {
                    if (biggestOdd != 0) {
                        count += biggestOdd - 1;
                    }
                    biggestOdd = entry.getValue();
                }
            }
        }

        System.out.println(map);
        return count+biggestOdd;
    }
}

"""
--- Submission ---

Runtime: 10 ms, Beats 9.97% of users with Java
Memory: 43.99 MB, Beats 5.39%of users with Java
"""