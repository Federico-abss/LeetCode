class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses = {n: [] for n in range(numCourses)}

        while prerequisites:
            for idx, prereq in enumerate(prerequisites):
                courses[prereq[0]].append(prereq[1])
                
            newPrerequisites = []
            noPrereq = set()
            for key, value in courses.items():
                if not value:
                    noPrereq.add(key)
                else:
                    courses[key] = []
                    
            for key in noPrereq:
                courses.pop(key)
                    
            for prerequisite in prerequisites:
                if prerequisite[1] not in noPrereq:
                    newPrerequisites.append(prerequisite)
                    
            if prerequisites == newPrerequisites:
                return False
            prerequisites = newPrerequisites
            
        return True