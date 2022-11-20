for i in range(1,10):
    j=i
    if j>5:
        j=10-j
    for k in range(1,j+1):
        print("*",end=" ")
    print("")