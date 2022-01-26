# Factorial question
from email.mime import base


def Factorial(A):
    base=1
    while A>=1:
        base=base*A
        A=A-1
    return base

print("Factorial is:",Factorial(6))