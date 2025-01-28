//https://softeer.ai/app/assessment/index.html?xid=355341&xsrfToken=58o4PqQWgIS7l7faqU0PLHeUaFSzwQSt&testType=practice
//X Marks the Spot

let n = Int(readLine()!)!
var charArr: [Character] = []
for i in 0..<n {    
    let words = Array(readLine()!.split(separator: " "))
    let index = Array(words[0].lowercased()).firstIndex(of: "x")!
    let letter = Array(words[1])[index]
    charArr.append(letter)
    }

print(String(charArr).uppercased())