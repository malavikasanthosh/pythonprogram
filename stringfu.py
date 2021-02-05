from stringop import rev
from stringop import upper
from stringop import palind
from stringop import pangram

s=input('enter the string:')
print('reverse of the string:',rev(s))

s=input("enter the string:")
upper(s)

s=input("enter the string:")
palind(s)

string=input("enter the string:")
if(pangram(string)):
    print("pangram")
else:
    print("not pangram")




