n=int(input())
c=0
for i in range(1,int(n/2)+1):
    if n%i==0:
        c+=1
print(c)