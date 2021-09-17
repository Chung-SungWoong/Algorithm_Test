#8x8 체스판에 특정한 위치에 있는 나이트가 움직일 수 있는 경우의 수
#수평으로 2칸 이동 후 수직으로 한 칸 or 수직으로 두 칸 이동 후 수평으로 한 칸
#책의 정답

n = input()
row = int(n[1])
column = int(ord(n[0]) - int(ord('a'))) + 1
count = 0
step = [(2,1), (2, -1), (-2,1), (-2,-1), (1,2),(1,-2),(-1,2),(-1,-2)]

for i in range(len(step)):
    ch = (column, row) + step[i]
    if ch[0] < 1 or ch[0] > 8 or ch[1] < 1 or ch[1] > 8:
        count -= 1
    count += 1


print(count)
