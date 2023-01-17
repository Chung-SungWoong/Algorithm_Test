"""
정규표현식 정리
"""

import re

p = re.compile("[a-zA-Z]+")

print(p.match('ab1sc123'))
print(p.match('123bad'))

n = ("^x") # 문자열의 시작을 표현, 여기서는 x로 시작하는 문자열을 의미
n = ("x$") # 문자열의 종료를 표현, 여기서는 x로 종료되는 문자열을 의미
n = (".x") # 임의의 한 문자의 자리수를 표현 문자열이 x로 끝난다는 것을 의미
n = ("x+") # 반복을 표현하며 x문자가 한번 이상 반복됨을 의미
n = ("x?") # 존재여부를 표현, x가 존재할 수도, 존재하지 않을 수도 있음을 의미
n = ("x*") # 반복여부를 표현, x가 0번 또는 그 이상 반복됨을 의미
n = ("x|y") # or 를 표현하며 x 또는 y 문자가 존재함을 의미
n = ("(x)") # 그룹을 표현, x를 그룹으로 처리함을 의미
n = ("(x)(y)") # 그룹들의 집합을 표현, 앞순부터 번호를 부여하여 관리하고 각 그룹의 데이터로 관리
n = ("(x)(?:y)") # 그룹들의 집합에 대한 예외를 표현, 그룹 집합으로 관리되지 않음을 의미
n = ("x{n}") # 반복을 표현하며 x문자가 n번 반복됨을 의미
n = ("x{n,}") # 반복을 표현하며 x문자가 n번 이상 반복됨을 의미
n = ("x{n,m}") # 반복을 표현하며 x문자가 최소 n번 이상 m번 이하로 반복됨을 의미

n = ("[xy]") # 문자 선택을 표현하며 x와 y중에 하나를 의미