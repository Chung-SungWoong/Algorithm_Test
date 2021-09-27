"""
DFS 소스코드 예제
"""

def dfs(graph, v, visited):
    visited[v] = True           #해당 노드를 확인 했다라는 뜻
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:      #재귀적으로 노드를 탐색
            dfs(graph, i, visited)


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9           # graph의 노드가 연결된 정보를 표현할 때 첫번째 인덱스는 공란으로 놔두어 노드의 숫자 그대로 매핑하는 편이 더 낫다.

dfs(graph, 1, visited)