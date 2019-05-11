import sys

try:
    fout = open('output.txt','w')
    a = sys.argv[1]
    b = [0]
    if int(a) > 0:
        a = int(a)
        for i in range(a):
            b.append(b[i]+i)
        for j in range(len(b)):
            if b[j]%2==1 and b[j]<a and b[j]!=1:
                print(b[j],end=", ",file=fout)
    else:
        print("The given number was not positive!")
    fout.close
except ValueError:
    print("The given character was not a number!")