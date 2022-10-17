"""
최대와 최소
"""


def bigger(x, y):
    if x < y:
        return y
    elif y < x:
        return x 
    else:
        print("both number are same")

print(bigger(5, 3))