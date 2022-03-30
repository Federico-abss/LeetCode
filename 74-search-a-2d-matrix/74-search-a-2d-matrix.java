class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int j = 0;
        int i = 0;
        int height = matrix.length - 1;
        int width = matrix[0].length - 1;
        int current = matrix[0][0];
        int right;
        int below;
        
        while (i <= width) {
            if (current > target) {
                break;
            } else if (current == target) {
                return true;
            } else {
                if (j < height) {
                    below = matrix[j+1][i];
                    if (below <= target) {
                        j++;
                        current = below;
                        continue;
                    } 
                } 
                if (i < width) {
                    right = matrix[j][i+1];
                    current = right;
                }
                i++;
            }
        }
        
        return false;
    }
}