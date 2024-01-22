#https://www.acmicpc.net/problem/11724

class Solution:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.parents = [i for i in range(self.n+1)]
        self.num_children = [1 for i in range(self.n+1)]
        self.num_components = self.n

    # collapsing find
    def find(self, v):
        parent = self.parents[v]
        if parent != v:
            self.parents[v] = self.find(parent)
            return self.parents[v]
        else:
            return v

    # weighted union
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root != v_root:
            if self.num_children[v_root] <= self.num_children[u_root]:
                self.parents[v_root] = u_root
                self.num_children[u_root] = self.num_children[u_root]+self.num_children[v_root]
            else:
                self.parents[u_root] = v_root
                self.num_children[v_root] = self.num_children[u_root] + self.num_children[v_root]
            self.num_components -= 1

instance = Solution()
for i in range(instance.m):
    u, v = map(int, input().split())
    instance.union(u, v)

print(instance.num_components)








