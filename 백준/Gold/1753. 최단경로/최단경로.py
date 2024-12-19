import sys
import heapq
input = sys.stdin.readline

def di(graph, start, n):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))
    return distance

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

answer = di(graph, start, n)
for i in range(1, n + 1):
    if answer[i] == float('inf'):
        print('INF')
    else:
        print(answer[i])