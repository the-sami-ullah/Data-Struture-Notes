#we use this algo. when we want order of nodes .. a is before b or not ?
# in this algo.
# we add nodes into stack until we found
# and then we reverse the  stack (FIFO) -  to get exact order of graph
# use recursive dfs algo 


from collections import defaultdict



graph = defaultdict(list)

# graph[u].append(v)

visited = set()
stack = []

def dfs(node):
    visited.add(node)

    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)

    stack.append(node)


for node in range(n):
    if node not in visited:
        dfs(node)


topo = stack[::-1]

print(topo)