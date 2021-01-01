class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        hmap = defaultdict(int)
        off = 0
        
        for ch in s:
            
            hmap[ch] += 1
            if hmap[ch] % 2:
                off += 1
            else:
                off -= 1
                
        return off == len(s) % 2
                
        
