//https://leetcode.com/problems/course-schedule-iv/description/
//Course Schedule IV

class Solution {
    func checkIfPrerequisite(_ numCourses: Int, _ prerequisites: [[Int]], _ queries: [[Int]]) -> [Bool] {
        var outgoingEdges: [[Int]] = Array(repeating: [], count: numCourses)
        var indegrees: [Int] = Array(repeating: 0, count: numCourses)
        for (i, prerequisite) in prerequisites.enumerated() {
            let a: Int = prerequisite[0]
            let b: Int = prerequisite[1]
            outgoingEdges[a].append(b)
            indegrees[b] += 1
        }

        var myqueue: [Int] = []
        for (i, indegree) in indegrees.enumerated() {
            if indegree == 0 {
                myqueue.append(i)
            }
        }
        
        var childrens: [Int: Set<Int>] = [:]
        for i in 0..<numCourses { 
            childrens[i, default: Set()].update(with: i)
        }

        while !myqueue.isEmpty {
            let curr = myqueue.removeFirst()
            for neighbor in outgoingEdges[curr] {
                childrens[neighbor, default: Set()].formUnion(childrens[curr, default: Set()])
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0 { 
                    myqueue.append(neighbor)
                }
            }
        }

        var answer: [Bool] = []
        for query in queries {
            let a = query[0]
            let b = query[1]
            if childrens[b, default: Set()].contains(a) {
                answer.append(true)
            } else {
                answer.append(false)
            }
        }
        
        return answer
    
    }
}