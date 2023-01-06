def add(num):
    return num+5
num=[10.33,23,66,43.88,12,32,32.22]
price=[10,24,56,20,18]
# new_price=[]
# for i in price:
#     new_price.append(add(i))
# print(new_price)
# new_price=map(add,price)
new_price=map(lambda n:n+5,price)
round_num=list(map(round,num))
print(list(new_price))
print(round_num)