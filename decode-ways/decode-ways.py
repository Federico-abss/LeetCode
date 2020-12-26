class Solution:
    def numDecodings(self, s: str) -> int:
        
        nset = {str(idx) for idx in range(1, 27)}
        
        @lru_cache()
        def decode(start = 0):
            
            if start == len(s):
                return 1
            
            if s[start] == "0":
                return 0
            
            res = decode(start + 1)
            if start < len(s) - 1 and s[start:start+2] in nset:
                res += decode(start + 2)
            
            return res
        
        return decode()
