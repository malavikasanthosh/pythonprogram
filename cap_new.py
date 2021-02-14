def capitalize(s):
    return s[0].upper()+s[1:]
try:
    inf=open('cap.txt')
    w=inf.read().split()
    p=""
    for x in w:
        out=capitalize(x)
        p=p+""+out
    print(p)
    inf.close()
except IOError as io:
    print(io)
