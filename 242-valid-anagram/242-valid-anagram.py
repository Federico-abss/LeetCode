class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counterS = Counter(s)
        counterC = Counter(t)
        return  counterC == counterS