// https://leetcode.com/problems/valid-parentheses/submissions/1532729992
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()) {
            switch (c) {
                case '(' -> stack.push(')');
                case '{' -> stack.push('}');
                case '[' -> stack.push(']');
                default -> {
                    if (stack.isEmpty()) {return false;}

                    Character pop = stack.pop();
                    if (!pop.equals(c)) {
                        return false;
                    }
                }
            } 
        } 
        if (stack.isEmpty()) {return true;}
        else {return false;}
    }
}