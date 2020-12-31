class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if not k:
            return 0
        if k >= len(s):
            return len(s)
        
        hmap = defaultdict(int)
        left = 0
        right = k
        res = k
        
        for ch in s[0: k]:
            
            hmap[ch] += 1
            
            
        while right < len(s):
            l, r = s[left], s[right]
            hmap[r] += 1
            if len(hmap) <= k:
                res += 1
            else:
                hmap[l] -= 1
                if not hmap[l]:
                    hmap.pop(l)
                    
                left += 1
            right += 1
            
            
        return res
        
