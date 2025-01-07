# 파이썬 숫자형 사용법
# 데이터 타입 선언
# 연산자 활용
# 형 변환
# 외부 모듈 사용 (삼각함수, 반올림, 원주율 등)

# 1. 파이썬 지원 자료형
# int : 정수
# float : 실수
# complex : 복소수
# bool : 불린 (참 or 거짓)
# str : 문자열(시퀀스)
# list : 리스트(시퀀스)
# tuple : 튜플(시퀀스)(순서에 따른 데이터)
# set : 집합
# dict : 사전

# 2. 데이터 타입
str1 = 'Python'
bool = True
str2 = 'Anaconda'
float = 10.0
int = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}

print(type(list))
print(str1)
print(bool)
print(str2)
print(float)
print(type(dict))

tuple = (7, 8, 9)
# tuple은 괄호 없이도 선언 가능하나, 괄호 넣는것이 좋음.
set = {4, 5, 6}

print(set)
print(tuple)

tuple = (7, 8, 9)
set = {4, 5, 6}

# print 이후 라인에 선언할 경우 해당 값은 출력되지 않는 것인가?

# 3. 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) x ** y -> 2 ** 3
# pow는 괄호 안 x의 y제곱을 출력
# x ** y 와 같음.
# pow(2, 3) = 2 ** 3
"""

# 4. 정수 선언
i = 77
i2 = -14
big_int = 7777777777777777779999999999999

print(i)
print(i2)
print(big_int)
print()

# 5. 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()

# 6. 연산 test
i1 = 39
i2 = 939
big_int1 = 111189388491894893849890
big_int2 = 482938409123849182938198
f1 = 1.234
f2 = 3.939

# 6-1. 덧셈
print('>>>>>+')
print('i1 + i2 : ', i1 + i2)
print('f1 + f2 : ', f1 + f2)
print('big_int1 + big_int2 : ', big_int + big_int2)

# 6-2. 곱셈
print('i1 곱하기 i2 : ', i1 * i2)

# 형 변환 참고
# 서로 다른 형 계산시 자동으로 형이 변환됨
