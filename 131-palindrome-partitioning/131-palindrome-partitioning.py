@cache
def isPalindrome(s: str) -> bool:
    return s == s[::-1]
    
        
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        solutions = defaultdict(list)
        solutions[0] = [[]]
        for idx in range(len(s)):
            offset = idx+1
            while offset <= len(s):
                if isPalindrome(s[idx:offset]):
                    solutions[offset].extend([solution + [s[idx:offset]] for solution in solutions[idx]])

                offset += 1
        
        return solutions[len(s)]
        
        
            