# Chapter 2-1
# 파이썬 완전 기초
# Print 사용법

# 기본 출력
print('Python Start')
print("Python Start2")
print('''Python Start3''')
print("""Python Start4""")

# 개행
print()

# Separator
print('p', 'Y', 'T', 'H', 'O', 'N', sep=' / ')
print('python', 'google.com', 'sep=@')
 
# and option
print('welcome to', end=' ')
print('IT News', end=' ')
print('Website')

# file option
# stdout이란 콘솔 데이터를 추출하는 것
import sys
print('learn python', file=sys.stdout)

# format 사용 (d, s, f)
# d=digit(정수), s=문자열, f=float(소수)
# 문자열은 어떻게 넣어도 상관 무, 숫자열은 d/f 반드시 표기
print('%s %s %s' % ('one', 'two', 'three'))
print('{} {}'.format('one', 'two'))
print('{1} {0}' .format('하나', '둘'))

# %s 사용법
print('%10s' % ('일이삼사오륙칠팔구십'))
print('{:>10}' .format('아주나이스네'))
print()
print('%-10s' % ('일이삼사오륙칠팔구십'))
print('{:10}' .format('아주나이스네'))
# 바로 윗열 왜 자동으로 중앙정렬이 되었는지?

# 선택 문자로 채우기
print('{:_>10}' .format('아주나이스네'))

# 중앙 정렬
print('{:^10}' .format('아주나이스네'))

# 공간 확보 후 원하는 개수의 문자만 출력
print('%.5s' % ('아주나이스네'))
print('%5s' % ('아주나이스네'))
print('{:10.5}' .format('일이삼사오륙칠팔구십'))

# %d
print('%d %d' % (1,2))
print('%d %d %d' % (10,20,30))
print('{} {} {}' .format(1,2,3))
print('%4d' % (42))
print('{:4d}' .format(42))

# %f
print('%1.18f' % (3.14659210101014342345))
print('{:4d}' .format(42))

print('%07.3f' % (3.146592653589793))
print('{:07.3f}' .format(3.14649201051378897))
# 지정 소수점 n자리에서 자동으로 반올림 하는듯?