"""
연결리스트 
숫자가 입력되면 리스트에 저장
0이 입력되면 제일 오래된 숫자 pop
음수가 입력되면 프로그램 종료
단 리스트에 숫자가 남아있다면 마지막에 다 출력
"""

l = []

while True:
    n = int(input("숫자를 입력하세요"))
    if n > 0:
        l.append(n)
    elif n == 0:
        print(l.pop())
    else:
        print(l)
        break
"""
위의 코드를 재귀 함수를 이용하여 바꾸기
"""

