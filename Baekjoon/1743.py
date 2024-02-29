"""
https://www.acmicpc.net/problem/1743

BFS
"""

def BFS(MAP, N, M, visited, strpnt):

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    Q = deque()
    Q.appendleft(strpnt)

    cnt = 1
    while Q:
        x, y = Q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and MAP[nx][ny] == 1:
                visited[nx][ny] = 1
                Q.appendleft((nx, ny))
                cnt += 1
    return cnt

if __name__ == "__main__":

    from collections import deque

    # NxM (hxw)
    N, M, K = map(int, input().split())

    MAP = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())

        MAP[x-1][y-1] = 1

    visited = [[0] * M for _ in range(N)]

    max = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and MAP[i][j] == 1:
                visited[i][j] = 1
                tmp = BFS(MAP, N, M, visited, (i, j))
                if max < tmp:
                    max = tmp
    print(tmp)