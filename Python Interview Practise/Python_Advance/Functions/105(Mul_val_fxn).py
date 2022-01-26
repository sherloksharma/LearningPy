from re import sub


def sum_sub_mul_div(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=sum_sub_mul_div(20,10)
x,y,a,b=sum_sub_mul_div(20,10)
print("Sum is:",x)
print("sub is: ",y)
print(a)
print(b)
print(type(t))
print(t)
print("The results are:")
for y in t:
    print(y)
    