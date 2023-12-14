/* 
--- Description ---

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 */

class Solution {
    public String convert(String s, int numRows) {
        String ans = "";
        if (numRows == 1) return s;
        
        for (int row=0;row < numRows;row++) {
            int col = 0;
            int index = row;
            int col_space = (numRows-1) * 2;
            int shift_index = row*2;
            while (index < s.length()) {
                ans += s.charAt(index);
                if (!(row == 0 || row == numRows-1)) {
                    if (col%2 == 0) index += col_space - shift_index;
                    else index += shift_index;
                } else index += col_space;
                col++;
            }
        }
        return ans;
    }
}

/* 
--- Submission ---

Runtime: 13ms [32.63%]
Memory: 44.74MB [18.92]
 */