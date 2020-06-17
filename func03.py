def fadd(n,m):
    s = n + m
    print(n, "+", m, "=", s)

while True:
    a = int(input("첫 번째 점수 입력 :"))
    b = int(input("두 번째 점수 입력 :"))

    if a==0 and b ==0 :
        break
    else:
        fadd(a, b)
