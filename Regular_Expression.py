"""

"""

import re

p = re.compile("[a-zA-Z]+")

print(p.match('ab1sc123'))
print(p.match('123bad'))

n = ("^x") # 문자열의 시작을 표현, 여기서는 x로 시작하는 문자열을 의미
n = ("x$") # 문자열의 종료를 표현, 여기서는 x로 종료되는 문자열을 의미
n = (".x") # 임의의 한 문자의 자리수를 표현 문자열이 x로 끝난다는 것을 의미