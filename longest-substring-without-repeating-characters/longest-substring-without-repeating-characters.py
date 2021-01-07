class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        start = 0
        end = 1
        hmap = defaultdict(int)
        hmap[s[0]] += 1
        
        while end < len(s):
            S, E = s[start], s[end]
            hmap[E] += 1
            if len(hmap) < end - start + 1:
                hmap[S] -= 1
                if not hmap[S]:
                    hmap.pop(S)
                
                start += 1
            end += 1
            
        return end - start
                
