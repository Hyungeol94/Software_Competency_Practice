from collections import deque
import copy
from typing import List


class Solution:
    def __init__(self, edges):
        self.edges = edges
        self.adjacency_list = self.get_adjacency_list()
        self.counts = list(map(
            lambda a: len(a[1]),
            self.adjacency_list.items()
        ))
        self.center_node = self.get_center_node()
        self.parents = self.union_find()

    def get_adjacency_list(self):
        adjacency_list = {}
        for edge in self.edges:
            a, b = edge
            adjacency_list[a] = adjacency_list[a] + [b] if adjacency_list.get(a) else [b] #단방향
        return adjacency_list

    #생성한 정점의 번호 구하기
    def get_center_node(self) -> int:
        ## 뻗어나오는 간선이 3 이상이라면 그곳이 센터임
        for i, count in enumerate(self.counts):
            if 3 <= count:
                return list(self.adjacency_list.items())[i][0]

        ## 뻗어나오는 간선이 2인 노드가 하나일 때
        if self.counts.count(2) == 1:
            return list(self.adjacency_list.items())[self.counts.index(2)][0]

        # 8자 그래프에도 뻗어나오는 간선의 개수가 2인 노드가 존재함. center_node와의 차이를 어떻게 구할까?
        # center_node에서 시작하면, 그 다음 노드에 뻗어나오는 간선의 개수가 2인 노드가 연달아서 나오는 경우가 존재함.
        # 8자 그래프에서는 그런 경우가 없음
        for i, count in enumerate(self.counts):
            if count == 2:
                start_node = list(self.adjacency_list)[i]
                adjacent_nodes = self.adjacency_list[start_node]
                for i, adj_node in enumerate(adjacent_nodes):
                    visited = {adj_node}
                    while True:
                        if not self.adjacency_list.get(adj_node):
                           break
                        if len(self.adjacency_list[adj_node]) == 2:
                            return start_node
                        adj_node = self.adjacency_list[adj_node][0]
                        if {adj_node} & visited:
                            break
                        visited = visited | {adj_node}


    def graph_type(self, root)->int:
        #traverse the graph and count the total node and edges
        #간선이 단방향이라서 ... 유니온 파인드를 해야만 가능할지도! starting point를 보장받지 못함

        def get_edge_count(root, parents):
            count = 0
            for i, node in enumerate(parents):
                if parents[node] == root and node in list(self.adjacency_list):
                    count += len(self.adjacency_list[node])
            return count


        parents = self.parents
        total_nodes = sum(list(map(lambda a:
                               1 if a == root else 0
                               , parents.values())))
        total_edges = get_edge_count(root, parents)


        #1은 도넛 모양 그래프, 노드의 개수 === 간선의 개수
        if total_nodes == total_edges:
            return 1
        #2는 막대 모양 그래프, 노드의 개수 -1 === 간선의 개수
        if total_nodes-1 == total_edges:
            return 2
        #3은 8자 모양 그래프, 노드의 개수 +1 === 간선의 개수
        if total_nodes+1 == total_edges:
            return 3


    def union_find(self):
        def union(a, b, parents):
            b_parent = find(b, parents)
            parents[a] = b_parent

        def find(a, parents):
            parent = parents[a] if parents.get(a) else a
            parents[a] = a if not parents.get(a) else parents[a]
            if a == parent:
                return parent
            else:
                #여기서 collapsing find가 일어나야 함
                parents[a] = find(parent, parents)
                return find(parent, parents)

        parents = {}
        adjacency_list_for_traverse = list(copy.deepcopy(self.adjacency_list))
        #union_find 초기 세팅
        adjacency_list_for_traverse.pop(adjacency_list_for_traverse.index(self.center_node))

        for i, [a, b] in enumerate(self.edges):
            parents[a] = a
            parents[b] = b

        parents.pop(self.center_node)

        for node in adjacency_list_for_traverse:
            next_nodes = self.adjacency_list[node]
            for i, next_node in enumerate(next_nodes):
                union(node, next_node, parents)

        for node in adjacency_list_for_traverse:
            find(node, parents)

        return parents


    def get_graph_counts(self) -> List[int]:
        center_node = self.center_node
        parents = self.parents
        roots = list(set(parents.values()))
        answer = [center_node, 0, 0, 0]
        for root in roots:
            answer[self.graph_type(root)] += 1
        return answer


def solution(edges):
    solution_instance = Solution(edges)
    return solution_instance.get_graph_counts()