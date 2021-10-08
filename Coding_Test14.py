def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        return False
    try:
        s = int(s)
        answer = True
    except:
        answer = False
    return answer


def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("a234") )
print( alpha_string46("1234") )