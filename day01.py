print('Python Starting...')
print('''안녕하세요
반갑습니다
어서오세요
사랑합니다''')
print("He's Python~~~~~")
print('He said, "Hello"')
print("오늘은", "혈맥강사를", "만나서", "파이썬을", "배웁니다")
print("오늘은 혈맥강사를 만나서 파이썬을 배웁니다")

# separator option
print('P', 'Y', 'T', 'H', 'O', 'N', sep='-')
print('010', '1234', '5678', sep='-')

# end option
print('Welcome to', end=' ')
print('Seop World')
print('example', end='@')
print('naver.com')

# format 사용 - %d(정수), %s(문자), %f(실수)
print('섭섭해님의 나이: {}이고 성별: {}입니다.'.format(50,'남자'))
print('섭섭해님의 나이: {1}이고 성별: {0}입니다.'.format('남자',50))
print('섭섭해님의 나이는 %d이고 성별은 %s 입니다.' %(50,'남자'))

#자릿수 지정 가능 %s
print('%10s' % ('nice' , )) #오른쪽부터 채워나감
print('%-10s' % ('nice' , )) #왼쪽부터 채워나감
print('%5s' % ('pythonstudy', )) #자릿수보다 초과되도 전체 데이터가 출력됨
print('%.5s' % ('pythonstudy', )) #.을 붙이면 자릿수만큼 절삭됨

#%d
print('%d %d' % (1,2)) #정수 2개 출력
print('%4d' % (42,)) #자릿수 지정
print('%-4d' % (42,)) #자릿수 지정

#%f
print('%f' % (3.1415926536, )) #소숫점 아래 6자리까지만 출력, 반올림
print('%1.2f' % (3.1415926536)) #정수부 + 소숫점 2자리까지만 출력, 반올림

#변수
'''
Python Built-In types
- Numeric
- Sequence
- Text Sequence
- Set
- Mapping
- Bool
- 파이썬에는 배열이 존재하지 않고 추후 배울 numpy에서 ndarray 타입이 파이썬의 배열이다.
'''
'''
변수를 선언하는 다양한 방법
- Camel  Case: numberOfCollegeGraduates, 첫문자를 소문자 (변수) - 권장
- Pascal Case: NumberOfCollegeGraduates, 첫문자를 대문자 (클래스)
- Snake  Case: number_Of_College_Graduates, 언더바 사용 (변수)
주의)
숫자로 시작할 수 없고, 특수문자 _와 $만 허용
대소문자를 구별한다.
예약어는 변수로 사용할 수 없다.
'''

print('변수 - ')
age = 10
Age = 20
print(age, Age, type(age), type(Age)) #int = Numeric

# keyword.py
# keyword.함수(), keyword.변수
import keyword
kw = keyword.kwlist
print('type - ', type(kw))
print('data - ', kw)

# 변수 바인딩 ('=' 연산자를 이용해서 할당)
year = 2022
month = 1
day = 25
print(year, month, day, type(year), type(month), type(day))
print('오늘은 {}년 {}월 {}일 입니다'.format(year, month, day))

year = '2022'
month = '1'
date = '25'
print(year, month, date, type(year), type(month), type(date))

intValue = 123
floatValue = 3.14
boolValue = True
strValue = 'jslim'
print('type - ', type(intValue), type(floatValue), type(boolValue), type(strValue))

print(intValue + floatValue)
print(intValue, strValue)

# 형변환
print(str(intValue) + strValue)
print(bool(str), type(bool(str)))
name = ''
print(int(bool(name)), type(int(bool(name)))) #값이 있음 = True = 1, 값이 없음 = False = 0