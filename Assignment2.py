n=int(input('enter number:'))
tot=0
while(n>0):
  dig=n%10
  tot=tot+dig
  n=n//10
  print('the total sum of digits is:',tot)
