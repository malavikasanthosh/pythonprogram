class login(Exception):pass
try:
   n=input('enter username:')
   p=input('enter password:')
   n1="adhy"
   p1="adhy@123"
   if n==n1 and p==p1:
          print('Login Successful')
   else:
          raise login('Login Unsuccessful')
except login as e:
     print(e)
