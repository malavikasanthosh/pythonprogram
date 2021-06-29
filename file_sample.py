with open('sample1.txt')as fi1,open('sample2.txt') as fi2:
    f1=fi1.readlines()
    f2=fi2.readlines()
    maxl=len(f1)if len(f1)>len(f2)else len(f2)
    for i in range(maxl):
        if i<len(f1) and i<len(f2):
            print(f1[i].strip()+' '+f2[i])
        elif i>=len(f1):
            print(f2[i])
        else:
            print(f1[i])
