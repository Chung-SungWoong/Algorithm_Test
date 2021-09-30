"""
<<<<<<< HEAD
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

제한사항
배열 arr의 크기 : 1,000,000 이하의 자연수
배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
입출력 예
arr	answer
[1,1,3,3,0,1,1]	[1,3,0,1]
[4,4,4,3,3]	[4,3]
"""
def solution(arr):
    answer = []
    print(len(arr))
    for i in range(len(arr)):
        if i+1 == len(arr):
            answer.append(arr[i])
            continue
        if arr[i] == arr[i+1]:
            continue
        else:
            answer.append(arr[i])
    
    return answer


print(solution([1,2,3,3,3,1,2]))


def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

print(no_continuous([1,3,4,2,2,4,4,1]))
=======
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
입출력 예 설명
입출력 예 #1

수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.
"""

def solution(answers):
    answer = []
    a = '12345'
    b = '21232425'
    c = '3311224455'
    count1 = 0
    count2 = 0
    count3 = 0
    total = []
    for i in range(len(answers)):
        if answers[i] == int(a[i%len(a)]):
            count1 += 1
        if answers[i] == int(b[i%len(b)]):
            count2 += 1
        if answers[i] == int(c[i%len(c)]):
            count3 += 1
    total.append(count1)
    total.append(count2)
    total.append(count3)
    winner = total.index(max(total))
    for j in range(len(total)):
        if total[winner] == total[j]:
            answer.append(j+1)
    
    return answer

    print(solution([1,2,3,4,5]))

    # 오늘 배운 것:
    """
    같은 숫자들이 반복 할 때 i%len(a) 식으로 비교하는 방법 생각해냄!
    a.index(max(a)) ====>>>>> index는()안에 있는 숫자의 위치를 찾는 함수, max(a)는 어레이 안에 있는 가장 큰 수를 찾는 함수

    다른 사람의 답:
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]               #스코어를 따로 기록하는 대신 하나의 리스트에 저장, 생각해보니 저렇게 하면 그냥 += 1 하면되서 편할 듯
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):             # 순서대로 비교해서 맥스 값과 같으면 어팬드
            result.append(idx+1)        # 사실상 나와의 큰 코드 차이는 없으나 더 깔끔하고 간략하게 만들어 놓은 코드 = 실력차이

    return result
    """
>>>>>>> ce525e2a7e570145bc4d429332bd1715d24a2ce0
