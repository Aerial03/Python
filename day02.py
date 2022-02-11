# 문자열이 제공하는 함수
# 파이썬의 모든 변수의 타입은 객체(instance)로 취급된다.

str01 = ''
str02 = str() #인스턴스 생성 구문
print('type - ', type(str01))

phoneNumber = "010-4603-2283"
str03 = phoneNumber.split("-") #문자열을 -를 기준으로 나누기
print('type - ', type(str03))
print('data - ', str03)

seqTxt = "Talk is cheap. Show me the code!!" #시퀀스 데이터
print('seqTxt - type, len', type(seqTxt), len(seqTxt))
print('dir - ', dir(seqTxt)) #객체가 가지고 있는 내장함수들을 보는 것

# 시퀀스 데이터는 인덱싱 및 슬라이싱이 가능하다.
# dir체크 시 __iter__가 있어야함
# 인덱싱: 인덱스 하나만 가져오기
# 슬라이싱: 특정 범위의 인덱스들을 가져오기
# [start : end-1 : step]
print('첫번째 단어 indexing - ', seqTxt[0]) #인덱싱
print('첫번째~네번째 단어들 slicing - ', seqTxt[0:4]) #마지막 인덱스는 +1
print('마이너스 indexing - ', seqTxt[-6])
print('마이너스 slicing - ', seqTxt[-6:-2])

exStr = "홀짝홀짝홀짝홀짝홀짝홀짝홀짝홀짝"
print('exStr 홀 - ', exStr[::2]) #step 2, 0번째부터 2칸씩
print('exStr 홀 - ', exStr[0:len(exStr):2]) #0과 len(exStr)은 생략가능
print('exStr 짝 - ', exStr[1::2])
print('exStr 짝홀 - ', exStr[::-1]) #step -1, 반대로

# 문자열이 가지고 있는 함수 소개
strSlicing = 'nice Python'
print('Capitalize - ', strSlicing.capitalize())

phoneNumber = "010-4603-2283"
print('replace - ', phoneNumber.replace('-', ' '))

url = 'http://www.naver.com'
print('url slicing - ', url[-3:])
print('url slicing - ', url[-3:], url[url.find('com'):])
print('url slicing - ', url[len(url)-3:])

urlLst = url.split('.')
print('urlLst type - ', type(urlLst), urlLst)

companyName = '    samsung    '
print('len - ', len(companyName))
print('data - ', companyName, len(companyName.strip()), companyName.lstrip(), companyName.rstrip())
#공백제거 함수

# upper(), lower()
print('upper - ', companyName.upper())

# 문자열 in 연산자를 이용해서 문자열을 판별할 수 있다.
fruitTxt = 'apple banana pineapple mango grape melon'
print('in operator - ', 'Apple'.lower() in fruitTxt)

drinking = 'cocacola'
print(len(drinking), drinking.count('c'), drinking.find('l'), drinking.index('a'))

# 확장자가 xls, xlsx 파일인지 여부를 확인하고 싶다면?
fileName = 'report.xls'
print('xls, xlsx 파일인지 여부 - ', fileName.endswith(('xls', 'xlsx')))
# 파일이름이 report인지를 판단하고 싶다면?
print('report 파일인지 여부 - ', fileName.startswith('report'))

'''
list (중요)
- array X
- 순서 O, 중복 O, 수정 O, 삭제 O
- index 0~
- 선언 [], list()
- [{key:value}, {}]
'''

lst = [1,2,3,4]
print('type - ', type(lst), lst)
print('dir - ', dir(lst))
print('indexing - ', lst[0])
print('slicing - ', lst[0:2])

lst = [1,2,3,4,'jslim',['show', 'me', 'the', 'code']]
print('me - ', lst[-1][1])

# 연산 가능
x = [1,2,3,4]
y = [4,5]
z = x + y
print('type - ', type(z), z)
z[0] = 0
print('type - ', type(z), z)

# list 가지고 있는 함수
z.append(7) #추가
print('append - ', z)
z.insert(1,6) #삽입
print('insert - ', z)
z.sort() #오름차순 정렬
print('sort - ', z)
z.reverse() #내림차순 정렬
print('reverse - ', z)
z.pop(0) #인덱스 값 삭제
print('pop - ', z)
del z[0] #인덱스 값 삭제
print('del - ', z)
z.remove(3) #데이터 삭제
print('remove - ', z)

# append() & extend()
lst01 = [1,2,3]
lst02 = [4,5]
lst01.append(lst02)
print('append - ', lst01)

lst03 = [1,2,3]
lst04 = [4,5]
lst03.extend(lst04)
print('extend - ', lst03)

# inner list
# [ [], [] ]
inner_lst = ['a', 'b', 'c']
outer_lst = [10, 3.14, True, 'string', inner_lst]
print('type - ', type(outer_lst))
print('data - ', outer_lst)
print('inner lst - ', outer_lst[-1][0])

# range(): 숫자를 순차적으로 생성해주는 객체
tmpRange = range(1,11)
print('range - ', type(tmpRange), tmpRange)
print('indexing - ', tmpRange[-1])
# in
print('in - ', 11 in tmpRange)

# 제어구문, 반복구문
# for ~ in: (반복)
# if ~ in: (조건제어)
for idx in tmpRange:
    print(idx, end = '\t')
print()

import random as r
tmpLst = []
for idx in range(5):
    tmpLst.append(r.randint(1,5))
print('data - ', tmpLst)

if 4 in tmpLst:
    print('in ok')
else:
    print('not in')

'''
list comprehension
- list 안에 for 구문을 포함
- 변수 = [ 실행문 for 변수 in sequence형 객체 ]
'''
x = [2,4,1,5,3]
result = []
for value in x:
    sqrt = value ** 2
    result.append(sqrt)
print('result - ', result)
result = [value**2 for value in x]
print('comprehension - ', result)
lst = [i*i for i in x] # 내 코드
print(lst)

'''
튜플(tuple)
- 선언: (), tuple()
- 순서 O, 중복 O, 수정 X, 삭제 X - 불변
- 읽기 전용
- indexing, slicing 가능
'''

tpl = (3,) # 원소가 1개여도 ,를 붙여야함
print('type - ', type(tpl), tpl)

tpl = 1,2,3,4,5,6
print('type - ', type(tpl), tpl)
print('indexing - ', tpl[0], type(tpl[0]))
print('slicing - ', tpl[0:2], type(tpl[0:2]))
# tpl [0] = 10 error, 수정 불가
# 캐스팅(형변환)을 통한 데이터 조작은 가능하다.
lst = list(tpl) # 리스트로 형변환
print('lst type - ', type(lst), lst)
lst[0] = 10 # 수정
tpl = tuple(lst) # 다시 튜플로 형변환
print('tpl type - ', type(tpl), tpl)

# 1~99까지의 정수 중 짝수만 튜플에 저장한다면?
tpl = tuple(range(2,100,2))
print(tpl)

# packing & unpacking
packing = ('A', 'B', 'C', 'D', 'E')
x1, x2, x3, x4, x5 = packing # 개수가 다르면 오류
print('type - ', x1, x2, x3, x4, x5)

packing = ('A', 'B', 'C', 'D', 'E')
x1, x2, x3, *x4 = packing
print('type - ', type(x1), type(x2), type(x3), type(x4))
print('data - ', x1, x2, x3, x4)