//https://leetcode.com/problems/guess-number-higher-or-lower/
//374. Guess Number Higher or Lower

/** 
 * Forward declaration of guess API.
 * @param  num -> your guess number
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0 
 * func guess(_ num: Int) -> Int 
 */

class Solution : GuessGame {
    func guessNumber(_ n: Int) -> Int {
        var left = 0
        var right = n
        while true {
            let middle = (left + right) / 2 
            let guess = self.guess(middle)
            if guess == -1 { 
                right = middle - 1
            } else if guess == 1 {
                left = middle + 1
            } else { 
                return middle
            }
        }
    }
}