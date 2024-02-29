"""
https://www.acmicpc.net/problem/12851

Queue
"""

if __name__ == "__main__":

    from collections import deque

    MAXSIZE = 100000
    N, K = map(int, input().split())

    Q = deque()
    Q.append((N, 0))

    while Q:
        v, t = Q.pop()

        if v - 1 >= 0:
            Q.appendleft((v-1, t+1))
        
        if v + 1 <= MAXSIZE:
            Q.appendleft((v+1, t+1))
        
        if v * 2 <= MAXSIZE:
            Q.appendleft((v*2, t+1))

        if v - 1 == K or v + 1 == K or v * 2 == K:
            print(t+1)
            cnt = 1
            while Q:
                nv, nt = Q.pop()
                if t+1 == nt and nv == K:
                    cnt += 1
            print(cnt)