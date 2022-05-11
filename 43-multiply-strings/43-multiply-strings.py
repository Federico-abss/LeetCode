class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def multiplyHelper(num1: str, num2: str) -> str:
            result = 0
            for idx, digit in enumerate(num2[::-1]):
                result += int(digit) * int(num1) * pow(10, idx)
            
            return str(result)
        
            
        def sumHelper(num1: str, num2: str) -> str:
            remaining = 0
            if len(num1) > len(num2):
                num2 = "0" * (len(num1) - len(num2)) + num2
                
            elif len(num1) < len(num2):
                num1 = "0" * (len(num2) - len(num1)) + num1
                
            result = 0
            for idx, digits in enumerate(zip(num1[::-1], num2[::-1])):
                result += (int(digits[1]) + int(digits[0])) * pow(10, idx)
            
            return str(result)
                                                 
        res = ""                                         
        for idx, num in enumerate(num1[::-1]):
            res = sumHelper(res, multiplyHelper(num, num2) + "0" * idx)
            
        return res
                                                