class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        absPath = path.split("/")
        absPath = filter(lambda x: x, absPath)
        
        for directory in absPath:
            directory = directory.strip("/")
            if directory == ".":
                continue
            elif directory == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
                
        return "/" + "/".join(stack)
        