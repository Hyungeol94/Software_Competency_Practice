//https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=swift
//신고 결과 받기

import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    
    // init
    var incomingEdges: [String: Set<String>] = [:]
    for log in report { 
        let arr = log.split(separator: " ").map{String($0)}
        let agent = arr[0]
        let target = arr[1]
        incomingEdges[target, default: Set<String>()].update(with: agent)
    }
    
    var mailCount: [String: Int] = [:]
    for (subject, neighbors) in incomingEdges { 
        if k <= neighbors.count {
            for neighbor in neighbors { 
                mailCount[neighbor, default: 0] += 1
            }
        }
    }
    
    var answer: [Int] = []
    for id in id_list { 
        answer.append(mailCount[id, default: 0])
    }
    
    return answer
}