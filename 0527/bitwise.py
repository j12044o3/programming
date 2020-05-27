#비트 연산은 두 수의 각각의 비트를 연산해서 수를 내어주는 연산


a = int(input("첫 번 째 정수: "))
b = int(input("두 번 째 정수: "))

print(a, "~", b, "=>" , (~a))
print(a, "&", b, "=>" , (a&b))
print(a, "^", b, "=>" , (a^b))
print(a, "|", b, "=>" , (a|b))

#sift 연산자는 각 비트를 주어진 수 만큼 이동시키는 연산

print(a, "<<", b, "=", (a<<b))
print(a, ">>", b, "=", (a>>b))
