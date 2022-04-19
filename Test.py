def solution(id_list, report, k):
    answer = []
    reporter = []
    reported = []
    ban = []
    alarm = []

    del_redun = set(report)
    one_report = list(del_redun)

    reported = []
    for i in range(len(one_report)):
        check = one_report[i].split()
        reporter.append(check[0])
        reported.append(check[1])

    for j in id_list:
        num = reported.count(j)
        if num >= k:
            ban.append(j)    

    for m in ban:
        position  = [index for (index, item) in enumerate(reported) if item == m]
        for n in position:
            alarm.append(reporter[n])


    for last in id_list:
        answer.append(alarm.count(last))

    return answer