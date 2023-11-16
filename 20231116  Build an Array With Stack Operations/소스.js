//https://leetcode.com/problems/build-an-array-with-stack-operations/

var buildArray = function (target, n) {
  const answer = []
  let j = 0
  for (let i = 1; i <= n; i++) { // the stream
      if (target[j] !== i) {
          answer.push("Push")
          answer.push("Pop")
      }
      else {
          answer.push("Push")
          j = j + 1
      }
      if (j === target.length) {
          return answer
      }
  }
};