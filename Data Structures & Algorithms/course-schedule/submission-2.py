class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        for [x,y] in prerequisites:
            if x not in prereq:
                prereq[x] = []
            prereq[x].append(y)
        
        visiting =  set()
        completed = set()
        def helper(i):
            if i in completed:
                return True
            if i in visiting:
                return False
            
            visiting.add(i)

            for j in prereq.get(i,[]):
                if not helper(j):
                    return False
            
            visiting.remove(i)
            completed.add(i)
            
            return True


        for i in range(numCourses):
            if not helper(i):
                return False
        return True