class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        seen = defaultdict(int)
        
        def dfs(iterations, vowels):
            
            if iterations == n:
                return 1
            
            if seen[(iterations, vowels)]:
                return seen[(iterations, vowels)]
            
            paths = sum(dfs(iterations + 1, n + 1) for n in range(vowels))
            seen[(iterations, vowels)] = paths
            
            return paths
        
        return dfs(0, 5)
            
