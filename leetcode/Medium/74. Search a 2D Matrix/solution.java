// https://leetcode.com/problems/search-a-2d-matrix/submissions/1534917543
import java.util.List;

class Solution {
    
    public boolean binSearchMatrix(int[][] mat, int start, int end, int target) {
        while (start < end) {
            int mid = (start + end) / 2;
            int row = mid / mat[0].length;
            int col = mid % mat[0].length;
            if (mat[row][col] < target) {
                start = mid + 1;
            } else if (mat[row][col] > target) {
                end = mid;
            } else {
                return true;
            }
        }
        return false;
    }

    public boolean binSearch(List<Integer> arr, int start, int end, int target) {
        while (start < end) {
            int mid = (start + end) / 2;
            if (arr.get(mid) < target) {
                start = mid + 1;
            } else if (arr.get(mid) > target) {
                end = mid;
            } else {
                return true;
            }
        }
        return false;
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        // Append each row to each other to make a 1D matrix
        // List<Integer> new_array = new ArrayList<Integer>();
        // for (int[] row : matrix) {
        //     for (int n : row) {
        //         new_array.add(n);
        //     }
        // }
        // return binSearch(new_array, 0, new_array.size(), target);


        // Find a way to binary search through 2D
        // Use indices as if normal array, but parse to find row and column
        // row = int p / matrix[0].length - 1, col = int p % matrix[0].length - 1
        int len = matrix[0].length * matrix.length;
        return binSearchMatrix(matrix, 0, len, target);
    }
}