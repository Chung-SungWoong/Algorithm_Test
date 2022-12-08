def count(s):
    answer = []
    ratio = []
    grades = ['s',"a",'b','c']
    for grade in grades:
        answer.append(s.count(grade))
        ratio.append('{:0.2f}'.format(s.count(grade)/len(s)*100))
    """
    sum = 0 
    for i in range(len(ratio)):
        sum += float(ratio[i])
    print(sum)
    """
    return answer, ratio


print(count('asbbsaaasaassasasssasssasabbbaaacasaassasaaaassaaaabba'))