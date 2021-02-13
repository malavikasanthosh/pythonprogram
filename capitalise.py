try:
    inf=open('append.txt')
    for x in inf:
        out=x.title()
        print(out)
    inf.close()
except IOError as io:
    print(io)
