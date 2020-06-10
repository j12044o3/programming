e_s = 0
o_s = 0
for i in range(101):
    if i%2 == 0:
        e_s += i
    else:
        o_s += i
print("홀수 합 : ",o_s)
print("짝수 합 : ",e_s)
