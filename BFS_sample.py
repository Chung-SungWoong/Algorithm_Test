"""
미로 탈출
n x m 크기의 직사각형 형태의 미로에 갇혀 있다. 위치는 (1,1)이고 미로의 출구는 (n,m)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있다
이때 괴물이 있는 부분을 0으로 없는 부분을 1로 표시
이때 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오
"""

from collections import deque

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.poplef()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: