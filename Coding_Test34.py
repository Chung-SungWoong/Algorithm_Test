"""
신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.
각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
id_list	report	                                                                                        k	result
["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	                                    3	[0,0]
"""

def solution(id_list, report, k):
    answer = []
    reporter = []
    reported = []
    ban = []
    alarm = []
    position_set = [] 

    del_redun = set(report)         # set 사용하여 중복 제거
    one_report = list(del_redun)    # set은 순서가 매번 바뀜

    for i in range(len(one_report)):   
        check = one_report[i].split()    #스페이스를 기준으로 스플릿
        reporter.append(check[0])       #앞쪽을 리포터로 어팬드
        reported.append(check[1])       #뒤쪽을 리포티드로 어팬드

    for j in id_list:
        num = reported.count(j)
        if num >= k:                    #만약 k보다 신고당한 수가 많다면 밴 리스트에 어팬드
            ban.append(j)    

    for m in ban:               #밴 당한 맴버 포지션 찾기 = 리포터 포지션 찾기
        position  = [index for (index, item) in enumerate(reported) if item == m]
        position_set += position
    for n in position_set:      #리포터 포지션에 따라 리포터 찾아서 알람에 어팬드
        alarm.append(reporter[n])

    for last in id_list:        #리포터 수 카운트해서 id_list 순서에 따라 숫자 더해주기
        answer.append(alarm.count(last))

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi","muzi neo"],2))