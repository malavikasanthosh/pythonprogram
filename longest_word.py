try:
  inf=open('longfile.txt')
  word=inf.read().split()
  l=len(max(word,key=len))
  for i in word:
    if len(i)==l:
       print('Longest word:',i)
  inf.close()
except IOError as io:
  print(io)
