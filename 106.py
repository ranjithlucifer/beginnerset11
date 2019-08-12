am1,am2=map(int,input().split())
ame=input().split()
a=[]
for i in ame:
    if (int(i)%2)!=0:
        a.append(i)
print(a[am2-1])
