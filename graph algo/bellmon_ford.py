
#Bellman-Ford = Negative weights or negative-cycle detection
# Time complexity: O(V * E)


class Solution:
    def bellmanFord(self,V, edges, src):
    
            # Initially distance from source to all other vertices 
            # is not known(Infinite) e.g. 1e8.
            dist = [100000000] * V
            dist[src] = 0
        
            # Relaxation of all the edges V times, not (V - 1) as we
            # need one additional relaxation to detect negative cycle
            for i in range(V):
                for edge in edges:
                    u, v, wt = edge
                    if dist[u] != 100000000 and dist[u] + wt < dist[v]:
                        
                        # If this is the Vth relaxation, then there 
                        # is a negative cycle
                        if i == V - 1:
                            return [-1]
                        
                        # Update shortest distance to node v
                        dist[v] = dist[u] + wt
            return dist