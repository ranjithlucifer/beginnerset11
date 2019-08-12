n1,n2=map(int,input().split())
ame=list(map(int,input().split()[:n2]))
z=[]
for i in ame:
   if(i<=i+1):
     z.append(i)
print(z[n2-1])  
