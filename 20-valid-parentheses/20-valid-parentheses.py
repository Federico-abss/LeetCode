class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closing = {")": "(", "]": "[", "}": "{"}
        
        for br in s:
            if br in closing:
                if not stack or closing[br] != stack.pop():
                    return False
            else:
                stack.append(br)
        
        return len(stack) == 0
                