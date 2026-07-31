from collections import deque

def bfs(graph,src,N):

    visited = [False] * N 

    queue = deque([src])

    visited[src] = True

    while queue:
        node = queue.popleft()

        print(node)    
        for neighbour in graph[node]:
            if visited[neighbour] == False:
                visited[neighbour] = True
                queue.append(neighbour)
        