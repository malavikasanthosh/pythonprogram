try:
   n1=int(input('enter the numerator:'))
   n2=int(input('enter the denominator:'))
   print('%d / %d =%f'%(n1,n2,n1/n2))
except(ZeroDivisionError,ValueError)as e:
   print(e)
else:
   print('Division Successful')

