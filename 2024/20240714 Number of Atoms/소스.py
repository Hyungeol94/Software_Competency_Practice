from collections import defaultdict
from collections import deque


class Solution:
    def changeNum(self, s, n):
        mystack = []
        arr = deque(s)
        while arr:
            curr = arr.popleft()
            if curr.isnumeric():
                while arr and arr[0].isnumeric():
                    curr += arr.popleft()
                curr = str(int(curr)*n)
                mystack.append(curr)

            else:
                if arr and arr[0].islower():
                    curr += arr.popleft()
                if arr and not arr[0].isnumeric():
                    mystack.append(curr)
                    mystack.append(str(n))
                else:
                    if arr:
                        mystack.append(curr)
                    else:
                        mystack.append(curr)
                        mystack.append(str(n))

        return mystack

    def countOfAtoms(self, formula: str) -> str:
        mystack = []
        arr = deque(formula)
        while arr:
            curr = arr.popleft()
            if curr.isnumeric():
                while arr and arr[0].isnumeric():
                    curr += arr.popleft()
                if mystack[-1] == ')':
                    mystack.pop()
                    s = []
                    while mystack[-1] != '(':
                        c = mystack.pop()
                        s.append(c)
                    mystack.pop()
                    s = s[::-1]
                    s = ''.join(s)
                    s = self.changeNum(s, int(curr))
                    mystack += s
                else:
                    mystack.append(curr)
            else:
                if curr == ')':
                    if (not arr) or (arr and not arr[0].isnumeric()):
                        arr.appendleft('1')
                mystack.append(curr)
        
        print(mystack)
        freqDist = defaultdict(int)

        while mystack:
            num = mystack.pop()
            if not num.isnumeric():
                if num.islower():
                    num += mystack.pop()
                num = num[::-1]
                letter = num
                num = 1
                freqDist[letter] += int(num)
                continue

            letter = mystack.pop()
            if letter.islower():
                letter += mystack.pop()
                letter = letter[::-1]
            freqDist[letter] += int(num)

        s = ''
        for key, count in sorted(list(freqDist.items())):
            s += key
            s += str(count) if count != 1 else ''
    
        return s
        

                

    def countOfAtoms_fail(self, formula: str) -> str:
        ##숫자를 먼저 지우기
        mystack = []
        arr = deque(formula)
        while arr:
            curr = arr.popleft()
            if curr.isnumeric():
                while arr and arr[0].isnumeric():
                    curr += arr.popleft()
                if mystack[-1] == ')':
                    mystack.pop()
                    s = ''
                    while mystack[-1] != '(':
                        c = mystack.pop()
                        s += c
                    mystack.pop()
                    s = s[::-1]
                    mystack += list(s*(int(curr)))
                else:
                    if mystack[-1].islower():
                        mystack += list(mystack[-2:]*(int(curr)-1))
                    else:
                        mystack += list(mystack[-1]*(int(curr)-1))
            else:
                mystack.append(curr)
    
        freqDist = defaultdict(int)
        while mystack:
            curr = mystack.pop()
            if curr.islower():
                curr += mystack.pop()
                curr = curr[::-1]
                freqDist[curr] += 1
            else:
                freqDist[curr] += 1
        
        s = ''
        for key, count in sorted(list(freqDist.items())):
            s += key
            s += str(count) if count != 1 else ''
        
        return s

    

    ##두번째 시도 -> 괄호를 먼저 풀기 -> 카운트해서 넣기 