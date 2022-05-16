class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def charsAfterBackspace(s: str) -> List[str]:
            stack = []
            for char in s:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
                    
            return stack
                
        return charsAfterBackspace(s) == charsAfterBackspace(t)