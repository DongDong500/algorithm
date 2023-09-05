"""https://www.acmicpc.net/problem/1260

DFS/BFS
"""

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            for idx in reversed(list(graph[n] - set(visited))):
                stack.append(idx)
    return visited

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            for idx in sorted(list(graph[n] - set(visited))):
                queue.append(idx)
    return visited

if __name__ == "__main__":

    from collections import deque
    import sys

    G = {

    }

    # vertex, edge, starting vertex
    N, M, V = map(int, input().split())

    # initialize graph
    for i in range(N):
        G.update({ i+1 : set([])})

    # build graph
    for i in range(M):
        start, end = map(int, input().split())
        G[start] |= set([end])
        G[end] |= set([start])

    print("DFS:", DFS_with_adj_list(G, V))
    print("BFS:", BFS_with_adj_list(G, V))
    