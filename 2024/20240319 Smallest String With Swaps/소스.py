from copy import copy
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        #연결되어 있는 것들을 파악하기
        #연결되어 있는 것들끼리 정렬해서 return하기
        n = len(s)
        class DisjointSet:
            def __init__(self, n):
                self.parents =[i for i in range(n)]
                self.ranks = [1]*n

            def find(self, i): #collapsing find
                if self.parents[i] ==i :
                    return i
                root_i = self.find(self.parents[i])
                return root_i
            
            def union(self, k, v): #weighted union
                k_root = self.find(k)
                v_root = self.find(v)
                
                if self.ranks[k_root] > self.ranks[v_root]:
                    self.parents[v_root] = k_root
                
                if self.ranks[k_root] < self.ranks[v_root]:
                    self.parents[k_root] = v_root
                
                else:
                    self.ranks[k_root] += 1
                    self.parents[v_root] = k_root
        
        instance = DisjointSet(n)
        num_components = n
        for pair in pairs:
            if instance.find(pair[0]) != instance.find(pair[1]):
                instance.union(*pair)
                num_components  -= 1
        
        #root가 같은 node의 index를 모으기
        #순서는 바뀔 수 있어도 index는 바뀌면 안됨
        #index를 보존하면서.. 모아보기
        root_dict = {}
        for i, c in enumerate(s):
            root = instance.find(i)
            if root not in root_dict:
                root_dict[root] = [[i, c]]
            else:
                root_dict[root].append([i, c])
        
        swapHash = root_dict.copy()
        swapHash = {}
        for root, info in list(sorted(root_dict.items())):
            swapHash[root] = [list(zip(*info))[0], sorted(list(zip(*info))[1])]
        print(swapHash)

        charHash = {}
        for component in swapHash.values():
            [indices, chars] = component
            for index, char in list(zip(indices, chars)):
                charHash[index] = char
        
        charList = sorted(charHash.items())
        return ('').join(list(zip(*charList))[1])

