class Solution {
    public void nextPermutation(int[] nums) {
        int[] buckets = new int[101];
        
        // find first element on the left for next perm
        int curMax = 0;
        int i;
        for (i = nums.length-1; i >= 0; i--) {
            buckets[nums[i]] += 1;
            if (nums[i] > curMax) {
                curMax = nums[i];
            } else if (nums[i] < curMax) {
                int correctNum = curMax;
                int lastCorrectNum = curMax;
                while (--correctNum > nums[i]) {
                    if (buckets[correctNum] != 0) {
                        lastCorrectNum = correctNum;
                    }
                }
                nums[i] = lastCorrectNum;
                buckets[lastCorrectNum] -= 1;
                break;
            }
        }
        
        // insert elements in the right side of the array in sorted order 
        int bucketIdx = curMax;
        for (int j = nums.length-1; j > i; j--) {
            while (buckets[bucketIdx] == 0) {
                 bucketIdx--;
            }
            nums[j] = bucketIdx;
            buckets[bucketIdx] -= 1;
        }
    }
}