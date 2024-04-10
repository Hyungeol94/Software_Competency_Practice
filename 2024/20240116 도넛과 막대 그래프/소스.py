from collections import defaultdict

class DisjointSet:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    def find(self, i):
        if i not in self.parents:
            self.parents[i] = i

        if i == self.parents[i]:
            return i

        else:
            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]

    def get_rank(self, root_k):
        if root_k not in self.ranks:
            self.ranks[root_k] = 1
        return self.ranks[root_k]

    def union(self, k, v):
        root_k = self.find(k)
        root_v = self.find(v)

        rank_root_k = self.get_rank(root_k)
        rank_root_v = self.get_rank(root_v)

        if root_k == root_v:
            return

        if rank_root_k > rank_root_v:
            self.parents[root_v] = root_k

        if rank_root_k < rank_root_v:
            self.parents[root_k] = root_v

        if rank_root_k == rank_root_v:
            self.ranks[root_k] += 1
            self.parents[root_v] = root_k

def solution(edges):
    incoming_edges = defaultdict(list)
    outgoing_edges = defaultdict(list)
    adj_list = defaultdict(list)

    for k, v in edges:
        outgoing_edges[k].append(v)
        incoming_edges[v].append(k)
        adj_list[k].append(v)
        adj_list[v].append(k)

    #incoming edge가 없으며, outgoing edge가 2~3개인 노드가 생성한 정점!
    candidates = list(set(adj_list.keys())-set(incoming_edges.keys()))
    createdNode = None
    for candidate in candidates:
        if 2 <= len(outgoing_edges[candidate]):
            createdNode = candidate
            break

    #disjoint set을 만든 다음, root가 같은 그룹 내의 edge의 개수를 세기
    instance = DisjointSet()
    for k, v in edges:
        if k == createdNode:
            instance.find(v)
            continue
        instance.union(k, v)

    for key in instance.parents.keys():
        instance.find(key)

    edge_count = defaultdict(int)
    node_set = defaultdict(set)
    #동일한 root에 속하는 edge와 node를 세기
    for k, v in edges:
        root = instance.find(v)
        if k!=createdNode:
            edge_count[root] += 1
            node_set[root].add(k)
        node_set[root].add(v)

    answer = [createdNode, 0, 0, 0]
    for root, nodes in node_set.items():
        n = len(nodes)
        count = edge_count[root]
        if count == n:
            answer[1]+=1
        if count == n-1:
            answer[2]+=1
        if count == n+1:
            answer[3]+=1
    return answer


