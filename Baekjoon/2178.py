"""
https://www.acmicpc.net/problem/2178

BFS
"""

def BFS(MAP, N, M, strpnt):

    visited = [[0] * M for _ in range(N)]
    cnt = [[0] * M for _ in range(N)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    Q = deque()
    Q.appendleft(strpnt)

    cnt[strpnt[0]][strpnt[1]] = 1

    while Q:
        n, m = Q.pop()
        for i in range(4):
            dn = n + dx[i]
            dm = m + dy[i]
            if 0 <= dn < N and 0 <= dm < M and MAP[dn][dm] == 1 and visited[dn][dm] == 0:
                Q.appendleft((dn, dm))
                visited[dn][dm] = 1
                cnt[dn][dm] = cnt[n][m] + 1
    
    return cnt

if __name__ == "__main__":

    from collections import deque

    # (N, M)
    N, M = map(int, input().split())

    # NxM matrix
    MAP = [[int(i) for i in list(input())] for _ in range(N)]

    cnt = BFS(MAP, N, M, (0, 0))
    print(cnt[N-1][M-1])

