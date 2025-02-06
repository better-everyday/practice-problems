import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean isHappy(int n) {
        Set<Integer> path = new HashSet<Integer>();
        while (n != 1) {
            String number = String.valueOf(n);
            char[] digits = number.toCharArray();

            n = 0;
            for (char digit : digits) {
                int d = Character.getNumericValue(digit);
                n += Math.pow(d, 2);
            }

            if (!path.add(n)) {
                return false;
            }
        }
        return true;
    }
}