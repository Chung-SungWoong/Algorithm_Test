"""
1. 특정한 지점의 주변 상, 하, 좌, 우 를 살펴본 뒤에 주변 지점 중에서 값이 0이면서 아직 방문하지 않은 지점이 있담면 해당 지점을 방문한다.
2. 방문한 지점에서 다시 상 하 좌 우를 살펴보면서 방문을 다시 진행하면 연결되는 모든 지점을 방문할 수 있다
3. 1~2의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다
"""

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:      #주어진 범위를 벗어나는 경우 즉시 종료
        return False
    if graph[x][y] == 0:    #현재 노드를 아직 방문하지 않았다면 
        graph[x][y] = 1     #현재 노드 방문처리

        dfs(x -1,y)         #상하좌우의 위치도 모두 재귀적으로 호출
        dfs(x, y -1)
        dfs(x+1,y)
        dfs(x, y +1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)
