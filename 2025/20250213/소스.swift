//https://school.programmers.co.kr/learn/courses/30/lessons/12904?language=swift
//가장 긴 팰린드롬
import Foundation

func checkPalindromeLength(_ arr: [Character], _ i: Int) -> Int { 
    var left = i-1
    var right = i+1
    //그곳을 가운데로 하는 팰린드롬? 
    var count1 = 1 
    while 0 <= left && right < arr.count { 
        if arr[left] == arr[right] {
            left -= 1
            right += 1
            count1 += 2
        } else {
            break
        }
    }
    
    var count2 = 0
    //그곳을 중심의 오른쪽으로 하는 팰린드롬?
    left = i-1
    right = i
    while 0 <= left && right < arr.count { 
        if arr[left] == arr[right] {
            left -= 1
            right += 1
            count2 += 2
        } else {
            break
        }
    }
    return max(count1, count2)
}

func solution(_ s:String) -> Int {
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    let arrS = Array(s)
    var maxVal = 1
    for (i, _ ) in arrS.enumerated() { 
        maxVal = max(maxVal, checkPalindromeLength(arrS, i))
    }

    return maxVal
}