//https://leetcode.com/problems/make-number-of-distinct-characters-equal/description/
//2531. Make Number of Distinct Characters Equal

class Solution {
    func hasUniqueElement(_ keys: Set<Character>, _ freqDist: [Character: Int]) -> Bool { 
        for key in keys {
            if let value = freqDist[key], value == 1 { 
                return true
            }
        }
        return false
    }

    func hasEnoughElement(_ keys: Set<Character>, _ freqDist: [Character: Int]) -> Bool { 
        for key in keys { 
            if let value = freqDist[key], 2 <= value { 
                return true
            }
        }
        return false
    }

    func isItPossible(_ word1: String, _ word2: String) -> Bool {
        let word1Arr = Array(word1)
        let word2Arr = Array(word2)
        var word1FreqDist: [Character: Int] = [:]
        var word2FreqDist: [Character: Int] = [:]
        
        
        for c1 in word1Arr { 
            word1FreqDist[c1, default: 0] += 1
        }

        for c2 in word2Arr { 
            word2FreqDist[c2, default: 0] += 1 
        }


        var word1Set = Set(word1FreqDist.keys), word2Set = Set(word2FreqDist.keys)
        if word1Set.count < word2Set.count { 
            let temp = word1Set
            word1Set = word2Set
            word2Set = temp

            let temp2 = word1FreqDist
            word1FreqDist = word2FreqDist
            word2FreqDist = temp2
        }
        
        var diff1 = word1Set.subtracting(word2Set)
        var diff2 = word2Set.subtracting(word1Set)
        let common = word1Set.intersection(word2Set)
        let diff1HasUniqueElement = self.hasUniqueElement(diff1, word1FreqDist)
        let diff1HasEnoughElement = self.hasEnoughElement(diff1, word1FreqDist)
        let diff2HasUniqueElement = self.hasUniqueElement(diff2, word2FreqDist)
        let diff2HasEnoughElement = self.hasEnoughElement(diff2, word2FreqDist)
        let word1CommonHasUniqueElement = self.hasUniqueElement(common, word1FreqDist)
        let word1CommonHasEnoughElement = self.hasEnoughElement(common, word1FreqDist)
        let word2CommonHasUniqueElement = self.hasUniqueElement(common, word2FreqDist)
        let word2CommonHasEnoughElement = self.hasEnoughElement(common, word2FreqDist)


        if word1Set.count == word2Set.count {
            if 1 <= common.count { //common끼리 바꾸면 됨
                return true
            } else { // common이 존재하지 않는 경우
                 //두 셋에서 유일한 것이 모두 존재
                if diff1HasUniqueElement && diff2HasUniqueElement {
                    return true
                }
                //두 셋에서 유일한 것이 전무
                if !diff1HasUniqueElement && !diff2HasUniqueElement { 
                    return true
                }

                if diff1HasEnoughElement && diff2HasEnoughElement { 
                    return true
                }
                //그 외
                return false
            }
        } else if abs(word1Set.count - word2Set.count) == 1 { //거래를 해야 함

            if word1CommonHasUniqueElement && word2CommonHasEnoughElement {
                for key in common { 
                    if let value = word1FreqDist[key], value == 1 { 
                        for key2 in common { 
                            if key == key2 { 
                                continue
                            }
                            if let value2 = word2FreqDist[key2], 2 <= value2 { 
                                return true
                            }
                        }
                    }
                }
            //    return false
            }

            if diff1HasUniqueElement && word2CommonHasUniqueElement {
                return true
            }

            if diff1HasUniqueElement && diff2HasEnoughElement {
                return true
            }

            if diff1HasEnoughElement && word2CommonHasEnoughElement { 
                return true
            }

            return false
        } else if  abs(word1Set.count - word2Set.count) == 2{ //세트 자료구조에서 차이가 2 일때
            if diff1HasUniqueElement && word2CommonHasEnoughElement { 
                return true
            }
            return false
        } else { 
            return false
        }
    }
}
