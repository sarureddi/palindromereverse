num=input()
substring1=""
f=0
op1=[]
if num==num[::-1]:
  op1.append(0)
for x in range(len(num)-1):
  for y in range(x+1,len(num)):
    substring1=num[x:y+1]
    if substring1==substring1[::-1]:
      op1.append(len(num)-len(substring1))
     
print(min(op1))
