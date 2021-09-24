"""
입력을 위한 전형적인 소스코드
"""

n = int(input())

#   data = input()             78 82 64 321 12

#   data = input().split()    ['78','82','64','321',`12`]

data = list(map(int, input().split()))    # 숙달 해야함 


data.sort(reverse=True)
print(data)