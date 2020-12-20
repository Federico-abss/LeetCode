class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        
        decoded = {}
        lstring = 0
        factors = []
        
        for ch in S:
            
            if ch.isalpha():
                lstring += 1
                decoded[lstring] = ch
                
            else: 
                lstring *= int(ch)
                factors.append(int(ch))
        
        while not decoded.get(K, 0):
            
            if lstring == K:
                lstring //= factors.pop()
                K = lstring
                continue
            
            while K < lstring:
                while decoded.get(lstring, 0):
                    lstring -= 1
                lstring //= factors.pop()
                          
            i = 2
            while lstring * i < K:
                i += 1
            i -= 1
            K -= lstring * i
            
        return decoded[K]
