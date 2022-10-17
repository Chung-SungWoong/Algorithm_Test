def dfs(graph,v,visited):
    visited[v] = True       # 현재 노드를 방문처리
    print(v, end = ' ')

    for i in graph[v]:      # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i, visited)

graph = [ [], [2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [False] * 9
dfs(graph, 1, visited)


from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])          #큐 구현을 위해 deque 라이브러리 사용
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
graph = [ [], [2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False] * 9
bfs(graph,1,visited)