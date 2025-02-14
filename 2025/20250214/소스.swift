//https://leetcode.com/problems/product-of-the-last-k-numbers/
//1352. Product of the Last K Numbers

class ProductOfNumbers {
    var nums: [Int]
    var prefixes: [Int]
    var zeroIndices: [Int]

    init() {
        self.nums = []
        self.prefixes = []
        self.zeroIndices = []
    }
    
    func add(_ num: Int) {
        self.nums.append(num)
        if let last = self.prefixes.last, last != 0 { 
            self.prefixes.append(last * num)
        } else { //0인 경우 혹은 시작인 경우
            self.prefixes.append(num) 
        }
        if num == 0 { 
            self.zeroIndices.append(self.prefixes.count-1)
        }
    }
    
    func getProduct(_ k: Int) -> Int {
        let n = self.prefixes.count
        //n-k 안에 0이 있는지를 먼저 확인해야 함
        
        if let lastIndex = self.zeroIndices.last, n-1-k <= lastIndex && lastIndex <= n-1 { 
            return 0            
        }

        if n-1-k <= -1  {
            return self.prefixes[n-1]
        } else { 
            if self.prefixes[n-1-k] != 0 { 
                return self.prefixes[n-1] / self.prefixes[n-1-k]
            } 
            return self.prefixes[n-1]
        }
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * let obj = ProductOfNumbers()
 * obj.add(num)
 * let ret_2: Int = obj.getProduct(k)
 */
