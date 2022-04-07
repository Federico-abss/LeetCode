class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pQueue
            = new PriorityQueue<Integer>(
                Collections.reverseOrder());
        
        for (int stone : stones) {
            pQueue.add(stone);
        }
        while (pQueue.size() > 1) {
            int newStone = pQueue.poll() - pQueue.poll();
            if (newStone != 0) {
                pQueue.add(newStone);
            }
        }
        if (pQueue.size() > 0) {
            return pQueue.poll();
        }
        
        return 0;
    }
}