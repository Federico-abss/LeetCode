class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        hmap = defaultdict(list)
        for idx, num in enumerate(arr):
            hmap[num].append(idx)
            
        dq = deque([0])
        other = deque()
        visited = set([0])
        steps = 0
        while True:
            
            while dq:
            
                cur = dq.popleft()
                if cur == len(arr) - 1:
                    return steps
​
                if cur + 1 not in visited:
                    other.append(cur+1)
                    visited.add(cur+1)
                if cur - 1 > 0 and cur - 1 not in visited:
                    other.append(cur-1)
                    visited.add(cur-1)
​
                for i in hmap[arr[cur]]:
                    if i not in visited:
                        other.append(i)
                        visited.add(i)  
                hmap.pop(arr[cur])
                        
            steps += 1
            dq, other = other, dq
            
  
            
        
            
