"""
Check password
The password should be 8 ~ 12 long
composed with at least 1 letter, number and symbol (!@#$%^&*)
"""

sym = set('!@#$%^&*')
num = set('1234567890')

def check_Pass(s):
    if len(s) < 8 or len(s) > 12:
        return "Invalid Password"
    
    if all((c not in num) for c in s):
        return "Invalid Password"


    if all((i not in sym) for i in s):

        return "Invalid Password"

    return "Valid Password"


print(check_Pass("ImGdfa!3"))