//https://leetcode.com/problems/letter-tile-possibilities/
//1079. Letter Tile Possibilities

typealias FreqDist = [Character: Int]

class Solution {
    func dfs(_ freqDist: FreqDist, _ count: inout Int) { 
        for (key, value) in freqDist { 
            if 0 < value { 
                count += 1
                var newFreqDist = freqDist
                newFreqDist[key, default: 0] -= 1
                dfs(newFreqDist, &count)
            }
        }
    }

    func numTilePossibilities(_ tiles: String) -> Int {
        var freqDist: FreqDist = [:]
        for c in tiles { 
            freqDist[c, default: 0] += 1
        }

        var count = 0
        dfs(freqDist, &count)
        return count
    }
}