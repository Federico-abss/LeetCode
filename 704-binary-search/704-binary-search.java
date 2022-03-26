class Solution {
    public int search(int[] nums, int target) {   
        int leftBound = 0;
        int rightBound = nums.length;
        
        while (leftBound != rightBound) {
            int curIdx = leftBound + (rightBound - leftBound) / 2;
            int curNum = nums[curIdx];
            if (curNum == target) {
                return curIdx;
            }
            if (curNum > target) {
                rightBound = curIdx;
            } else {
                leftBound = curIdx + 1;
            }
        }
        
        return -1;
    }
}