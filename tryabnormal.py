try:
   n=int(input('enter an integer:'))
   if n<90 or n>120:
     raise ValueError('Abnormal Condition')
   print('Accepted Number')
except Exception as e:
   print(e)