class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        for [x,y] in prerequisites:
            if x not in prereq:
                prereq[x] = []
            prereq[x].append(y)
        
        done = set()
        pending = set()
        def helper(i):
            if i in done:
                return True
            if i in pending:
                return False
            
            pending.add(i)

            for j in prereq.get(i,[]):
                if not helper(j):
                    return False
            
            pending.remove(i)
            done.add(i)
            
            return True


        for i in range(numCourses):
            if not helper(i):
                return False
        return True