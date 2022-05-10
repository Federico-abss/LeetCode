class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        @cache
        def isPalindrome(subs: str) -> bool:
            return subs == subs[::-1]
                    
        for idx in range(len(s)):
            for jdx in range(idx, len(s)):
                count += isPalindrome(s[idx:jdx+1])
                    
        return count
                
        