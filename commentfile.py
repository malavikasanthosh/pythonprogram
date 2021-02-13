try:
  inf=open('comment.txt')
  line=inf.readlines()
  inf.close()
  outf=open('comment.txt','w')
  for x in line:
     if not (x.startswith('#')):
        outf.write(x)
  outf.close()
except IOError as io:
   print(io)