class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        result = [""]
        
        def helper(ch):
            return list(map(lambda x: x + ch, result))
            
        for ch in S:
            
            if ch.isnumeric():
                result = helper(ch)
            else:
                result = helper(ch.lower()) + helper(ch.upper())
            
        return result
                
                    
            