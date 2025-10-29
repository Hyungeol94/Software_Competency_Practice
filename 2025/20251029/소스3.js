//https://school.programmers.co.kr/learn/courses/30/lessons/68645
//삼각 달팽이

function solution(n) {
    const drs = [[1, 0], [0, 1], [-1, -1]] // 이렇게 반복함
    var dr_i = 0
    const matrix = []
    for (i = 0; i< n; i++ ) { 
        matrix.push(Array(i+1).fill(0))
    }
    
    const target = (1+n) * n / 2
    var count = 1
    var pos = [-1, 0]
    
    while (count <= target) {
        const next_pos = [pos[0]+drs[dr_i][0], pos[1]+drs[dr_i][1]]
        if (next_pos[0] < 0 || next_pos[0] >= n || next_pos[1] < 0 || next_pos[1] >= matrix[next_pos[0]].length ) { 
            dr_i = (dr_i + 1) % 3
            continue
        }
        if (matrix[next_pos[0]][next_pos[1]] != 0) { 
            dr_i = (dr_i + 1) % 3
            continue           
        }
        matrix[next_pos[0]][next_pos[1]] = count
        pos = next_pos
        count += 1
    }

    return matrix.flat()
}