import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, node):
    global count
    visited[node] = True
    order[node] = count
    count += 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
order = [0] * (n + 1)
count = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

dfs(graph, start)

for i in range(1, n + 1):
    print(order[i])