class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #다른 변수와의 관계에서 정해지는 값만이 주어짐
        
        class DisjointSet():
            def __init__(self):
                self.root_and_weight = {}
            
            def find(self, i):
                if i not in self.root_and_weight:
                    self.root_and_weight[i] = [i, 1]
                i_root, weight = self.root_and_weight[i]
                if i_root == i:
                    return self.root_and_weight[i]

                if i_root != i: #collapsing find
                    new_root, new_weight = self.find(i_root)
                    self.root_and_weight[i] = [new_root, weight*new_weight]
                return self.root_and_weight[i]

            def union(self, k, v, value):
                root_k, k_weight = self.find(k) #dividend
                root_v, v_weight = self.find(v) #divisor
                if root_k == root_v:
                    return
                
                #왼쪽에서 오른쪽으로 union하기
                new_root = root_v
                new_weight = value*v_weight/k_weight
                self.root_and_weight[root_k] = [new_root, new_weight]

  
               
        convert_table = {}    
        instance = DisjointSet()
        for equation, value in zip(equations, values):
            instance.union(*equation, value)

    
        answer = []
        for query in queries:
            if query[0] not in instance.root_and_weight or query[1] not in instance.root_and_weight:
                answer.append(-1)
                continue

            root_k, k_weight = instance.find(query[0])
            root_v, v_weight = instance.find(query[1])
            if root_k == root_v:
                #계산 가능
                #만약 a/b b/c c/d 순으로 연결되어 있다면? 
                #root를 찾아서 뭐할건데 ... 
                answer.append(k_weight/v_weight)

            else:
                answer.append(-1)
        return answer

                
                    

                
                

                    


                
            

                
            
                

