"""
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
첫째 줄에 정수 N이 입력 (0 =< N =< 23)
"""

n = map(int.input())
count = 0
sec, minute, Hour = 0
Total = 360 * n
char ti = ""
target = "3"

for i in range(Total):
    if target in ti:
        count += 1
    sec += 1
    if(sec == 60):
        sec = 0
        minute += 1
        if(minute == 60):
            minute = 0
            Hour += 1
    ti = char(Hour, minute, Hour)