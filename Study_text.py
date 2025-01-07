# 문자형 (매우 중요함)

# 1. 문자열 생성
str1 = 'Our hero hero'
str2 = 'the Dragonborn'
str3 = 'Comes'
str4 = """Dovahkiin"""
print()
print('Begin-----')
print(str1, str2, str3, str4)
print(type(str1))
print(len(str1), len(str2), len(str3), len(str4))
print()
print('----------')

# 2. 빈 문자열 만들기
str1_em = ''
str2_em = str() # 보다 고급 코드?

print(type(str1_em), type(str2_em))
print(len(str1_em), len(str2_em))
print()
print('----------')

# 3. 이스케이프 문자 사용 (따옴표 등)
# 따옴표 유형에 따라 문장 작성 필요함. 
# 역 슬래시 \를 앞에 붙인다.
# tab = \t
print("I'm a boy")
print('I\'m a boy')
print('A \t B')
print('AAA\nBBB')
print()

# 4. 
print('----------')
escape_str1 = "Do you visit \"The Cloud District\" often?"
escape_str2 = 'What\'s on the menu?'
print(escape_str1)
print(escape_str2)
print()

# 탭 및 줄바꿈
print('----------')
t1 = "We'll drive out \nThe Stormcloaks"
t2 = "\nAnd restore \nWhat we own"
t3 = "\nThe Age of Aggression \nIs just about done"

print(t1, t2, t3)
print()

# Raw String
# 문자열을 있는 그대로 출력해줌.
print('-----')
raw_s1 = r'D:\python\test'
print(raw_s1)