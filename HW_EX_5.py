a = [5,4,2,16,31,22,334,661,2131,6761,78745845,2222222222]
db = 0
for i in range(len(a)):
    if i!=len(a):
        if a[i]<a[i+1]:
            db += 1
print (db)