class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
       
        sortedPeople = sorted(people)
        
        i = 0
        j = len(people) - 1
        boats = 0
        
        while i <= j:
            
            light, heavy = sortedPeople[i], sortedPeople[j]
            if i == j:
                boats += 1
                break
                
            if heavy + light <= limit:
                i += 1
                
            j -= 1    
            boats += 1
            
        return boats
