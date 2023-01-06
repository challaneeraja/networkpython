def div(num):
    c=0
    if(num>=1):
        for i in range(1,num+1):
            if(num%i==0):
                c+=1
            return c
        if c==2:
            print("divisible by itself and 1")
        else:
            print("not divisible by itself and 1")
l=[2,3,4,5,6,7]
l1=[]
for p in l:
    l1.append(div(l))
print(l1)

