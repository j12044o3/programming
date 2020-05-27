#할당 연산은 오른쪽에 있는 수식(constant, variable, operator, function)
#을 연산하여 왼쪽에 있는 변수에 할당하는 연산자


a = int(input("첫 번째 정수 입력 : "))
b = int(input("두 번째 정수 입력 : "))

a = a + 1
print("a = b의 결과 ==>", (a))
a += b
print("a += b의 결과 ==>", (a))


# +, -, *, /, &, //, **
a <<= b
print("a <<= b의 결과 ==>", (a))

a &= b
print("a &= b의 결과 ==>", (a))
