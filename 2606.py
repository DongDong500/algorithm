"""
https://www.acmicpc.net/problem/2606

BFS
"""

def BFS(G):

    Q = deque([1])
    visited = []

    cnt = 0
    while Q:
        n = Q.pop()
        if n not in visited:
            visited.append(n)
            for idx in list(G[n] - set(visited)):
                Q.appendleft(idx)
                cnt += 1
    return cnt

if __name__ == "__main__":

    from collections import deque

    # number of computers
    N = int(input())

    # number of edges
    M = int(input())

    # initialize graph
    G = {}
    for i in range(N):
        G.update({i+1 : set()})

    for _ in range(M):
        a, b = map(int, input().split())
        G[a] |= set([b])
        G[b] |= set([a])
    
    print(BFS(G))
