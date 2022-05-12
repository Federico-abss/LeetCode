class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expandAroundCenter(l: int, r: int) -> int:
            
            result = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result = s[l:r+1]
                l -= 1
                r += 1
                
            return result
        
        result = ""
        for idx in range(len(s)):
            candidate1 = expandAroundCenter(idx, idx)
            candidate2 = expandAroundCenter(idx, idx+1)
            if len(candidate1) > len(result):
                result = candidate1
            if len(candidate2) > len(result):
                result = candidate2
            
        return result
        