#https://school.programmers.co.kr/learn/courses/30/lessons/150366
#표 병합

class DisjointSet:
    def __init__(self):
        self.parents = [i for i in range(50*50)]
        self.values = ["" for i in range(50*50)]
    
    
    def find(self, i): #collapsing find
        if self.parents[i] == i:
            return i
    
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]    
        
        
    def merge(self, k, v): 
        root_k = self.find(k)
        root_v = self.find(v)
        if root_k == root_v:
            return
        
        if not self.values[root_k] and self.values[root_v]:
            root_k, root_v = root_v, root_k

        self.parents[root_v] = root_k
        
    
    def update1(self, i, value): #루트값을 업데이트
        root_i = self.find(i)
        self.values[root_i] = value
    
    
    def update2(self, value1, value2):
        for i in range(50*50):
            root_i = self.find(i)
            if self.values[root_i] == value1:
                self.values[root_i] = value2 
        
        
    def unmerge(self, i):
        root_i = self.find(i)
        root_value = self.values[root_i]
    
        #루트를 모두 해제하고 자기 자신을 parent로 만든다
        nodes = []
        for j in range(50*50):
            if self.find(j) == root_i:
                nodes.append(j)
        
        for j in nodes:
            self.parents[j] = j
            self.values[j] = ""
                
        self.values[i] = root_value

        
def convert(r, c):
    return (int(r)-1)*50 + (int(c)-1)


def solution(commands):
    disjointSet = DisjointSet()
    answer = []
        
    for command in commands:
        parts = command.split()
        action = parts[0]
        if action == "UPDATE":
            if len(parts) == 4:
                _, r, c, value = parts
                i = convert(r, c)
                disjointSet.update1(i, value)
                
            else:
                _, value1, value2 = parts
                disjointSet.update2(value1, value2)
            
        elif action == "MERGE":
            _, r1, c1, r2, c2 = parts
            k = convert(r1, c1)
            v = convert(r2, c2)
            disjointSet.merge(k, v)
            
        
        elif action == "UNMERGE":
            _, r, c = parts
            i = convert(r, c)
            disjointSet.unmerge(i)
            
            
        elif action == "PRINT":
            _, r, c = parts
            i = convert(r, c)
            root_i = disjointSet.find(i)
            value = disjointSet.values[root_i]
            if value == "":
                answer.append("EMPTY")
            else:
                answer.append(value)
            
    return answer