# Chapter 02-2
# 변수 스터디

# 기본 선언
n = 700

print(type(n))

# 동시 선언
x = y = z = 700

print(x, y, z)

# 1. 선언
var = 75

# 2. 재선언
var = 'change value'

# 3. 출력
# 문자형으로 출력됨은 변수가 덮어씌워졌음을 의미함.
print(var)
print(type(var))

# Object reference
# 변수 값이 할당된 상태일 때
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1
print(300)
print(int(300))

# 예2
n = 777
print(n, type(n))

m = n

print()
print(m, n)
print(type(m), type(n))
print()

m = 400
m = n
print(m, n)
print(type(m), type(n))
print()

# id(identity) 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

m = 800
n = 800
z = 800
i = 800

print(id(m) == id(n))
# MEMO
# 위 4개 변수는 동일한 인스턴스
# 서로 다른 변수에 같은 값이 할당된 경우 하나의 값으로 간주함. 

# 다양한 변수 선언
# Camel Case : numberofCollege (소문자로 시작, 새 단어마다 대문자) -> Method 선언
# Pascal Case : NumberOfCollege (대문자로 시작, 새 단어마다 대문자) -> Class 선언
# Snake Case : number_of_college -> 파이썬에서 변수를 선언할 때 쓰임.
# 주로 

# 허용하는 변수 선언 방법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

NumberOfCollege = 3
print(NumberOfCollege)

# 예약어는 변수 명으로 지정할 수 없음
# 'as', 'for' 등 예약어는 설정 불가능
# python reserved words


