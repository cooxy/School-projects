def Expon(x):
    n = x
    q = 0
    a = []
    if n % 2 == 1:
        a.append(1)
    max = 0
    while q!=1 or q!=0:
        for i in range(1,n+1):
            if 2**i<=n:
                max = 2**i
        q = n - max
        a.append(max)
    print(a)





#main
try:
    n = int(input("Please give a positive number: "))
    if n<=0:
        print ("The given number was not positive!")
    else:
        Expon(n)
except ValueError:
    print("The given character was not a number!")