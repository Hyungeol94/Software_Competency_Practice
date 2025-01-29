//https://school.programmers.co.kr/learn/courses/30/lessons/12941
//최솟값 만들기

import Foundation

func solution(_ A:[Int], _ B:[Int]) -> Int
{
    let sortedA = A.sorted {$0 < $1}
    let sortedB = B.sorted {$0 < $1}
    var acc = 0
    
    for (a, b) in zip(sortedA, sortedB.reversed()) { 
        acc += a * b
    }
    return acc
}