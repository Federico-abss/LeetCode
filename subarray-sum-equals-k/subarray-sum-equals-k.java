class Solution {
    public int subarraySum(int[] nums, int k) {
        
        Map<Integer, Integer> hmap = new HashMap<>();
        hmap.put(0,1);
        int count = 0, currSum = 0;
        
        for (int num: nums) {
            
            currSum += num;
            
            count += hmap.getOrDefault(currSum - k, 0);
            
            hmap.put(currSum, hmap.getOrDefault(currSum, 0) + 1);
            
        }
        
        return count;
    }
}