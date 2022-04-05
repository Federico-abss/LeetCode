class Solution {
    public int maxArea(int[] height) {
        
        int start = 0;
        int end = height.length-1;
        int curMax = 0;
        while (start != end) {
            curMax = Math.max(curMax, computeVolume(height, start, end));
            if (height[start] < height[end]) {
                start++;
            } else {
                end--;
            }
        }
        
        return curMax;
    }
                              
    private int computeVolume(int[] height, int start, int end) {
        return Math.min(height[start], height[end]) * (end - start);
    }
}