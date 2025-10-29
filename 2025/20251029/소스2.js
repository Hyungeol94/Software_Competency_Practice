function getArr(arr, row, col, width) { 
    res = []
    for (i = row; i < row+width; i++) { 
        temp = []
        for (j =col; j< col+width; j++) { 
            temp.push(arr[i][j])
        }
        res.push(temp)
    }
    return res
}


function isCompressible(arr) { //압축가능한지 확인
    const num = arr[0][0]
    for (const [i, row] of arr.entries()){ 
        for (const [j, item] of row.entries()) { 
            if (num != item ) {
                return false
            }
        }
    }
    return true
} 


function solution(arr) {
    if (arr.length == 1) {
        return arr[0][0] == 0 ? [1, 0] : [0, 1]
    } 
    if (isCompressible(arr)) { 
        return arr[0][0] == 0 ? [1, 0] : [0, 1]
    }
    
    const mid = arr.length / 2
    const ans = [0, 0]
    for (const i of [0, mid]) { 
        for (const j of [0, mid]) { 
            const curr = getArr(arr, i, j, mid)
            const res = solution(curr)
            ans[0] += res[0]
            ans[1] += res[1]
        }  
    }
    return ans
}