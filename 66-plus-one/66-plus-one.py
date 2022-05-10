class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        number = int("".join(map(str, digits))) + 1
        
        for idx, ch in enumerate(str(number)):
            if idx < len(digits):
                digits[idx] = int(ch)
            else:
                digits.append(int(ch))
                
        return digits
        