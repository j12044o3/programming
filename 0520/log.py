#논리 연산자 (논리값을 연산하여 논리값을 산출하는 연산)
#논리값, boolean value (True, False)

a = input("첫 번째 논리값(True, False) 입력 : ")
b = input("두 번째 논리값(True, False) 입력 : ")

print("논리 부정(True->False, False->True) nota",(not(a)))
print("논리곱(둘 중에 하나라도 False이면 False) a and b", (a and b))
print("논리합(둘 중에 하나라도 Ture이면 Ture) a or b", (a or b))
