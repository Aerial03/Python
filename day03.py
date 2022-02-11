'''
dic(딕셔너리) 사전 자료형
범용적으로 가장 많이 사용
[{key:value},{}]
선언: {key:value}, dict()
sequence X, mapping O, 인덱싱과 슬라이싱 X
순서 X, 키 중복 X, 수정 O, 삭제 O
'''

tmpDict = {
    'name' : 'jslim',
    'phone' : '01046032283',
    'birth' : 730910
}
print('type - ', type(tmpDict), tmpDict)

# in 연산자 - 키 유무를 확인하는 용도로 사용 가능
print('key 검사 - ', 'name' in tmpDict)

tmpDict = {
    '메로나' : [300,20],
    '비비빅' : [400,20],
    '죠스바' : [100,50]
}
# 메로나의 정보를 확인하고 싶다면?
print('메로나의 가격은 {}원 입니다. '.format(tmpDict['메로나'][0]))
print('메로나의 수량은 {}개 입니다. '.format(tmpDict['메로나'][1]))

# 새로운 데이터를 추가하고 싶다면?
tmpDict['메로나'] = [500,50] #동일한 키를 추가하면 수정이 됨, 키 중복 X
print('data - ', tmpDict)
tmpDict['스크류바'] = [200,40] #새로운 키를 추가
print('data - ', tmpDict)

# 메로나의 가격을 10% 인상하고자 한다면?
tmpDict['메로나'][0] = tmpDict['메로나'][0]*1.1
print('data - ', tmpDict)

tmpDict = dict([
    ('city', 'seoul'), ('age', 50)
])
print('type - ', type(tmpDict), tmpDict)

# case 03
tmpDict = dict(
    city = 'seoul',
    age = 50
)
print('type - ', type(tmpDict), tmpDict)
print('key를 이용한 값 출력 - ', tmpDict['city'])
# print('key를 이용한 값 출력 - ', tmpDict['City']) 없는 키일 경우 error
print('key를 이용한 값 출력 - ', tmpDict.get('age'))
print('key를 이용한 값 출력 - ', tmpDict.get('Age')) #없는 키여도 error X, None
tmpDict.update({'name' : '임정섭'}) # 추가하는 함수
print('data - ', tmpDict)

# zip()
# case 04
keys = ('apple', 'pear', 'peach')
values = (1000,1500,2000)
zipDict = dict(zip(keys, values))
print('type - ', type(zipDict), zipDict)

# zip()을 안쓸 경우
zipDict = {}
for idx in range(len(keys)):
    zipDict[keys[idx]] = values[idx]
print('type - ', type(zipDict), zipDict)

# dict 소유의 함수 - keys(), values(), items() -> 반복문 사용 가능
for key in zipDict.keys():
    print(key)
for value in zipDict.values():
    print(value)
for key, value in zipDict.items():
    print('{}:{}'.format(key, value))

# pop()
print('pop - ', zipDict.pop('apple'))
print('data - ', zipDict)

zipDict.clear()
print('clear - ', zipDict)

'''
set 집합의 자료형
- 선언: {}, set()
- 순서X, 중복 X, 인덱싱과 슬라이싱 X
'''
tmpSet = {1,2,3,3,3,3,3,'jslim'}
tmpSet = set([1,2,3,3,3,3,3,'jslim'])
print('type - ', type(tmpSet), tmpSet)
print('dir - ', dir(tmpSet))
tmpT = tuple(tmpSet)
print('type - ', type(tmpT), tmpT)
tmpL = list(tmpSet)
print('type - ', type(tmpL), tmpL)

gender = ['남','남','여','남','남','여','남','남','여']
sgender = set(gender)
print('중복 제거 - ', type(sgender), sgender)

set01 = set('jslim')
print('set01 - ', set01)

set02 = set([1,2,3,4,5])
set03 = set([3,4,5,6,7])

print('교집합 - ', set02.intersection(set03))
print('합집합 - ', set02.union(set03))
print('차집합 - ', set02.difference(set03))

set02.add(6) # 1개만
print('add - ', set02)

set02.update([7,8]) # 여러개
print('update - ', set02)

set02.remove(6)
print('remove - ', set02)

set02.clear()
print('clear - ', set02)

'''
boolean Type
- True | False
- 논리연산자(not, and, or)
- 비교연산자( ~ ,  & , | )
- "", [], (), {}, 0, None -> False
'''
print('boolean - ', bool(0))
print('boolean - ', type([]), bool([]))

trueFlag = True
falseFlag = False
print('T and T - ', trueFlag & trueFlag)
print('T and F - ', trueFlag and falseFlag)
print('F and T - ', falseFlag and trueFlag)
print('F and F - ', falseFlag and falseFlag)
print()
print('T or T - ', trueFlag | trueFlag)
print('T or F - ', trueFlag or falseFlag)
print('F or T - ', falseFlag or trueFlag)
print('F ore F - ', falseFlag or falseFlag)

print('not - ', not trueFlag)
print('int - ', int(trueFlag))

'''
날짜
'''
     #pakage           #module       #function
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
     #pakage     #module             #function
from dateutil.parser import parse

# timedelta -> week, day, hour, minute, second
# relativedelta -> year, month

today = date.today()
print('type - ', type(today), today)
print(today.year, today.month, today.day)

day_time = datetime.today()
print('type - ', type(day_time), day_time)
print(day_time.hour, day_time.minute, day_time.second, day_time.microsecond)

today = date.today()
day = timedelta(days=-1)
print('하루 전 날짜 - ', type(today), type(day), today+day)

today = date.today()
day = relativedelta(months=-2)
print('2년 전 날짜 - ', today+day)

myDate = parse("2021-01-27 13:15:55")
print('type - ', type(myDate), myDate)

myDate = datetime(2019, 12, 25, 14, 21, 30)
print('type - ', type(myDate), myDate)

# 날짜 타입을 문자열 포맷으로 지정할 수 있다. %m %d %y %h %m %s
# strftime(날짜 -> 문자), strptime(문자 -> 날짜)
print('format - ', myDate.strftime("%m-%d-%y"))
print('날짜 -> 문자 - ', myDate.strftime("%m-%d-%Y"), type(myDate.strftime("%m-%d-%Y")))
str = "2019-12-25"
print('문자 -> 날짜 - ', datetime.strptime(str,'%Y-%m-%d'), type(datetime.strptime(str,'%Y-%m-%d')))

'''
사용자 입력
- input()
'''
name = input('Enter your Name: ')
age = int(input('Enter your Age: '))
height = float(input('Enter your Height: '))
marriage = input('Enter your Marriage: ')
if 'yes' in marriage:
    print('Marriage - True')
elif 'no' in marriage:
    print('Marriage - False')
else:
    print('Marriage - 오류')

print('input name - ', type(name), name)
print('input age - ', type(age), age)
print('input height - ', type(height), height)
print('input marriage - ', type(marriage), marriage)
print('end----------------------------------')