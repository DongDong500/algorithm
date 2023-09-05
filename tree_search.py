

if __name__ == "__main__":

    graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
    root_node = 1

    from collections import deque

    def BFS_with_adj_list(graph, root):
        visited = []
        queue = deque([root])

        while queue:
            n = queue.popleft()
            if n not in visited:
                visited.append(n)
                queue += graph[n] - set(visited)
        return visited
    
    print("BFS: ", BFS_with_adj_list(graph_list, root_node))

    def DFS_with_adj_list(graph, root):
        visited = []
        stack = [root]

        while stack:
            n = stack.pop()
            if n not in visited:
                visited.append(n)
                stack += graph[n] - set(visited)
        return visited

    print("DFS: ", DFS_with_adj_list(graph_list, root_node))