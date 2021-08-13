n=int(input())
p=int(input())
l=[]
m=[]
s=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
    
for j in range(1,p+1):
    if(p%j==0):
        m.append(j)

for i in l:
    for j in m:
        if(i==j):
            s.append(i)

print(s[-1])
            
