"""
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.
"""
def prim(G, node_n, start):
    import heapq
    # 방문기록용 리스트 생성
    visit = [False for _ in range(node_n)]
    visit[start] = True # 초기 노드 방문처리
    Q = []
    for k, v in G[start].items():
        heapq.heappush(Q, (v, k))
    w_sum = 0

    while Q: # 큐가 비어있으면 반복 종료
        now_cost,now_nodeB = heapq.heappop(Q) # 가장 우선순위가 높은것 pop
        if not visit[now_nodeB]: # pop된 노드가 방문된적 있는지 검사
            visit[now_nodeB] = True # 없다면 방문하고 방문표시
            w_sum += now_cost # 해당 노드로 가는 간선거리 추가
            for node_b,cost in G[now_nodeB].items(): # 해당 노드로부터 갈 수 있는 노드 큐에 삽입
                heapq.heappush(Q,(cost,node_b))
                
    # print(w_sum)
    return w_sum

def solution(n, costs):
    answer = 0

    G = {}
    for i in range(n):
        G[i] = {}
    
    for idx, c in enumerate(costs):
        nodefrom, nodeto, w = c
        if nodeto not in G[nodefrom].keys():
            G[nodefrom][nodeto] = w
            G[nodeto][nodefrom] = w
    
    # from math import inf
    min = 10000000
    for i in range(n):
        w = prim(G, n, i)
        if min >= w:
            min = w
    answer = min

    return answer



if __name__ == "__main__":
    N = [
        4
    ]
    costs = [
        [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    ]
    result = [
        4
    ]
    for n, c, rst in zip(N, costs, result):
        print(solution(n, c) == rst)