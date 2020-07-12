from typing import List

# i.e. find a hamiltonian cycle (NP)
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    prereq_list = {}
    visited = set()
    not_visited = set()
    stack = []
    # construct an adjacency list
    for course in prerequisites:
        if course[0] in prereq_list:
            prereq_list[course[0]] += [course[1]]
        else:
            prereq_list[course[0]] = [course[1]]

    print(prereq_list)
    for i in range(numCourses):
        not_visited.add(i)
    

if __name__ == "__main__":
    prereq = [[1,0], [2,0]]
    print(canFinish(3, prereq))