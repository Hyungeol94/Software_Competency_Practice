#https://academy.elice.io/courses/78960/lectures/639680/lecturepages/7122028
#철도 공사

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def getLines(self, n, queries):
        #init original line
        mydict = {}
        prev = None
        for i in range(n):
            node = Node(i+1)
            if prev:
                prev.right = node
            node.left = prev
            mydict[i+1] = node
            prev = node
        mydict[-1] = None

        #do the queries
        for query in queries:
            command = query[0]
            if command == 0: #폐쇄
                node_key = query[1]
                node = mydict[node_key]
                lefthand_node = node.left
                righthand_node = node.right
                node.left = None
                node.right = None
                if lefthand_node:
                    lefthand_node.right = righthand_node
                if righthand_node:
                    righthand_node.left = lefthand_node

            elif command == 1: #연결
                _, node_key, lefthand_node_key, righthand_node_key = query
                node, lefthand_node, righthand_node = mydict[node_key], mydict[lefthand_node_key], mydict[righthand_node_key]

                if lefthand_node:
                    node.left = lefthand_node
                    lefthand_node.right = node

                if righthand_node:
                    node.right = righthand_node
                    righthand_node.left = node
        
        res = []
        curr = mydict[1]
        while curr:
            res.append(curr.val)
            curr = curr.left
        res = res[::-1]

        curr = mydict[1].right
        while curr:
            res.append(curr.val)
            curr = curr.right
        
        return res


n, m = list(map(int, input().split()))
queries = []
for _ in range(m):
    query = list(map(int, input().split()))
    queries.append(query)

instance = Solution()
res = instance.getLines(n, queries)
print(" ".join(list(map(str, res))))