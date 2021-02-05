def rev(s):
  return s[::-1]

def upper(s):
   d={"upper":0,"lower":0}
   for x in s:
      if x.isupper():
          d["upper"]+=1
          
      elif x.islower():
          d["lower"]+=1
   print("uppercase:",d["upper"])
   print("lowercase:",d["lower"])

def palind(s):
    if s==s[::-1]:
        print('palindrome')
    else:
        print('not palindrome')

def pangram(s):
    if len(set('abcdefghijklmnopqrstuvwxyz')-set(s.lower()))==0:
        return True

    return False




  

