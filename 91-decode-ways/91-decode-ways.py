class Solution:
    def numDecodings(self, s: str) -> int:
        chars = {str(n) for n in range(1,27)}
        
        @cache
        def recursive_helper(s: str) -> int:
            if s and s[0] == '0':
                return 0
            
            result = 0
            for idx, ch in enumerate(s):
                if ch == '0':
                    return result
                print(s, result)
                if idx < len(s) - 1 and s[idx:idx+2] in chars:
                    result += recursive_helper(s[idx+2:])
                
            return result + 1
        
        return recursive_helper(s)
            
        