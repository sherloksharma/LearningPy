# Variable Length Arguements
def add(*n):
    total=0
    for x in n:
        total=total+x
    print("TheSum=",total)
add()
add(0,9)
add(0,87,87)

    