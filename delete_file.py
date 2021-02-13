try:
    w=input('Enter the word:')
    inf=open('file1.txt')
    line=inf.readlines()
    inf.close()
    out=open('file2.txt','w')
    for i in line:
        if w not in i.strip("\n"):
            out.write(i)
    out.close()
except IOError as io:
    print(io)
