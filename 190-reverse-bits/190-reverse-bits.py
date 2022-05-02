class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for shift in range(32):
            result <<= 1
            isSignificantBit = n & 1 << shift
            result |= 1 if isSignificantBit else 0
            
        return result