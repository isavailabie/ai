def fpath(n, edges):
    INF = float('inf')
    graph = [[] for _ in range(n + 1)]
    
    for u, v, w in edges:
        graph[u].append((v, w))
    
    dist = [INF] * (n + 1)
    dist[1] = 0 
    
    vis = [False] * (n + 1)
    
    for _ in range(n):  
        u = -1
        for i in range(1, n + 1):
            if not vis[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        
        if dist[u] == INF:
            break
        
        vis[u] = True
        
        for v, w in graph[u]:
            if not vis[v]:  
                dist[v] = min(dist[v], dist[u] + w)
        if dist[n] != INF:
            return dist[n]
        else:
            return -1



n, m = map(int, input().split())

edges = []  
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c)) 


print(fpath(n, edges))
