class Solution:
    def calculate(self, s: str) -> int:
        
        nums = deque(["0"])
        operations = deque()
        
        for ch in s:
            if ch.isnumeric():
                nums[-1] += ch
            elif ch != " ":
                operations.append(ch)
                nums.append("0")
                
        result = 0
        sign = 1
        
        # def calculateRecursive(nums: List[str]) -> int: 
        while nums:       
            cur = int(nums.popleft())
            while operations and (operations[0] == "*" or operations[0] == "/"):
                operator = operations.popleft()
                if operator == "*":
                    cur *= int(nums.popleft())
                else:
                    cur //= int(nums.popleft())
            
            result += sign*cur
            sign = 1
            
            if operations and operations.popleft() == "-":
                sign = -1
                
        return result
                
            
                