#https://school.programmers.co.kr/learn/courses/30/lessons/388354
#홀짝트리

import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict
from functools import lru_cache


class CountTree:
    def __init__(self, adj_list):
        self.adj_list = adj_list
        self.numChildren = defaultdict(int)
        for node, neighbors in adj_list.items():
            self.numChildren[node] = len(neighbors) - 1
    
    @lru_cache(maxsize=None)
    def isTree(self, root, node): #자식노드일 때, 홀짝 트리인지, 혹은 역홀짝 트리인지를 계산하기
        if node % 2 == 0: #짝수일 때
            if self.numChildren[node] % 2 != 0: #홀수라면
                return False

            if self.numChildren[node] == 0: #리프노드일 때
                return True

        else: #홀수일 때
            if self.numChildren[node] % 2 == 0: #짝수라면
                return False

            if self.numChildren[node] == 0: #리프노드일 때 (자식 노드의 개수가 짝수)
                return False

        for neighbor in self.adj_list[node]: 
            if neighbor == root: #부모는 제외하기
                continue

            if not self.isTree(node, neighbor):
                return False
        return True
            
    @lru_cache(maxsize=None)   
    def isOppositeTree(self, root, node):
        if node % 2 == 0: #짝수일 때
            if self.numChildren[node] % 2 == 0: #짝수라면
                return False

            if self.numChildren[node] == 0: #리프노드일 때
                return False

        else: #홀수일 때
            if self.numChildren[node] % 2 != 0: #홀수라면
                return False

            if self.numChildren[node] == 0: #리프노드일 때 (자식 노드의 개수가 짝수)
                return True


        for neighbor in self.adj_list[node]: 
            if neighbor == root: #부모는 제외하기
                continue

            if not self.isOppositeTree(node, neighbor):
                return False
        return True
    

def solution(nodes, edges):
    #포레스트로 주어짐, 분리할 필요 있음
    adj_list = defaultdict(list)
    for node in nodes:
        adj_list[node] = []
        
    for edge in edges:
        k, v = edge
        adj_list[k].append(v)
        adj_list[v].append(k)
    
    instance = CountTree(adj_list)
    
    #자식노드일 때, 홀짝 트리인지, 혹은 역홀짝 트리인지를 계산하기
    treeCount = 0
    oppositeTreeCount = 0

    for node in nodes:
        instance.numChildren[node] += 1
        if instance.isTree(-1, node):
            treeCount += 1
        if instance.isOppositeTree(-1, node):
            oppositeTreeCount += 1
        instance.numChildren[node] -= 1
    
    return [treeCount, oppositeTreeCount]