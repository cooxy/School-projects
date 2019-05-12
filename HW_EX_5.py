def ascend(ls):
    f = []
    if ls[1]>ls[0]:
        f.append(ls[0])
    for i in range(len(ls)-1):
        if ls[i+1]<=ls[i]:
            continue
        else:
            f.append(ls[i+1])
    print(("{} ({})").format(len(f),f))


#main
lst = [2,3,516,61,6712,321,61,17617173247,3243126236324,11111111111111111111111111111]
ascend(lst)
