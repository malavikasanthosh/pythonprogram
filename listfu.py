from listop import unique
from listop import square
n=input('enter list:')
l=n.split()
l=[int(j) for j in l]
print('list:',l)
print('unique list:')
unique(l)
print('square of list:')
square(l)
