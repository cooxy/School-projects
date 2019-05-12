def Expon(x):
    ls = []
    for i in range(x,0,-1):
        if 2**i<=x:
            ls.append(2**i)
            x -= 2**i
    if x % 2 == 1:
        ls.append(1)
    ls = ls[::-1]
    return (ls)

#main
try:
    n = int(input("Please give a positive number: "))
    if n<=0:
        print ("The given number was not positive!")
    else:
        print(Expon(n))
except ValueError:
    print("The given character was not a number!")
