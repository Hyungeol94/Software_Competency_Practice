//https://leetcode.com/problems/design-a-number-container-system/
//2349. Design a Number Container System

class NumberContainers {
    func findInsertionPoint(_ left: Int, _ right: Int, _ target: Int, _ nums: [Int]) -> Int { 
    if left > right {
        return left
    }
    
    let middle = (left + right) / 2
    
    if nums[middle] < target {
        return findInsertionPoint(middle + 1, right, target, nums)
    } else {
        return findInsertionPoint(left, middle - 1, target, nums)
    }
}


    func binarySearch(_ left: Int, _ right: Int, _ target: Int, _ nums: [Int]) -> Int { 
        let middle: Int = (left + right) / 2 
        if nums[middle] == target { 
            return middle
        } else if target < nums[middle] { 
            return self.binarySearch(left, middle, target, nums)
        } else { 
            return self.binarySearch(middle+1, right, target, nums)
        }
    }

    var indexMap: [Int: Int]
    var numberIndices: [Int: [Int]]

    init() {
        self.indexMap = [:]
        self.numberIndices = [:]
    }
    
    func change(_ index: Int, _ number: Int) {
        if let prev = self.indexMap[index] {
            //binarySearch
            //찾아서 없애기
            var indices = self.numberIndices[prev, default: []]
            var i = self.binarySearch(0, indices.count-1, index, indices)
            indices.remove(at: i) //logn이 걸림
            self.numberIndices[prev] = indices
        }

        self.indexMap[index] = number
        var indices = self.numberIndices[number, default: []]
        var i = self.findInsertionPoint(0, indices.count-1, index, indices)
        indices.insert(index, at: i)
        self.numberIndices[number] = indices
        // self.numberIndices[number, default: []].append(index)
        // self.numberIndices[number, default: []].sort() //최대 nlogn 걸림 .. 
    }
    
    func find(_ number: Int) -> Int {
        if let indices = self.numberIndices[number], !indices.isEmpty { 
            return indices[0]
        }
        return -1
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * let obj = NumberContainers()
 * obj.change(index, number)
 * let ret_2: Int = obj.find(number)
 */