"""
상하좌우
N X N 크기의 정사각형 공간. 가장 왼쪽 위 좌표는 1,1 가장 오른쪽 아래 좌표는 n,n에 해당
(R,L,U,D)로 적힌 여행계획서가 있을 때 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오
입력 예시             출력 예시
5                   3  4
R R R U D D
"""

n = 5
x, y = 1, 1
plans = "R R R U D D"

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x,y = nx, ny

print(x,y)

