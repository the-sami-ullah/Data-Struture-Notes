# Whenever a LeetCode problem asks something like:

# Find the minimum cost
# Find the shortest distance
# Find the least time
# Find the minimum effort
# Find the cheapest route

# and

# the graph has non-negative weights.      


#  Time complexity:
# Adjacency List + Min Heap

# Time: O((V + E) log V)
# Heap operations (push/pop) cost O(log V).
# Across the algorithm, you process all vertices and inspect all edges.(V + E)



class Solution:
    def dijkstra(self, V, edges, src):

        graph = {}

        for i in range(V):
            graph[i] = []

        # Undirected graph
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        import heapq

        heap = []

        distance = {}

        for node in graph:
            distance[node] = float('inf')

        distance[src] = 0

        heapq.heappush(heap, (0, src))

        while heap:

            current_distance, node = heapq.heappop(heap)

            # most important line of code of dijkstra
            if current_distance > distance[node]:
                continue

            # (neighbor, weight)
            for neighbour, weight in graph[node]:

                new_distance = current_distance + weight

                if new_distance < distance[neighbour]:

                    distance[neighbour] = new_distance

                    heapq.heappush(heap, (new_distance, neighbour))

        return [distance[i] for i in range(V)]

