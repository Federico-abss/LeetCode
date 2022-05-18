class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleanS = list(map(lambda x: x.lower(), filter(lambda x: x.isalnum(), s)))
        return cleanS == cleanS[::-1]