"""
대기번호 관리하는 프로그램
숫자가 입력되면 큐에 저장하고 0이 입력되면 큐에서 가장 오래 기다린 대기번호를 꺼내어 출력한다
0보다 작은 숫자가 입력되면 프로그램 종료
큐가 비었으면 queue empty 를 출력
"""

que = []

while True:
    n = int(input("input number: "))
    if n > 0:
        que.append(n)
    elif n == 0:
        que.pop()
    else:
        print("프로그램 종료!")
        break
    
    if len(que) == 0:
        print("Queue empty!")