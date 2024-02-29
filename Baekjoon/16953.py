"""
https://www.acmicpc.net/problem/16953

Queue
"""

if __name__ == "__main__":

    from collections import deque

    A, B = map(int, input().split())

    Q = deque()
    Q.append((A, 1))

    flag = 0
    while Q:
        v, t = Q.pop()

        if v == B:
            print(t)
            flag = 1
            break

        if v * 2 <= B:
            Q.appendleft((v*2, t+1))
        
        if v * 10 + 1 <= B:
            Q.appendleft((v*10+1, t+1))
    
    if flag == 0:
        print(-1)