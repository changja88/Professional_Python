# 문자열 포맷팅


# 1. 숫자 바로 대입
print("I eat %d apples" % 3)

# 2. 문자열 바로 대입
print('I eat %s apples' % 'five')

# 3. 2개 이상 값 넣기
number = 10
day = 'three'
print('I ate %d apples per %s days' % (number, day))

# 문자열 포맷 코드
# - %s : 문자열
# - %c : 문자 1개
# - %d : 정수
# - %f : 부동소수


# 이름으로 넣기
print(
    'I ate {number} apples. So I was sick for {day} days'.format(number=10, day=3)
)

# f 문자열 포맷팅
# - 파이썬 3.6. 부터는 f문자열 포맷팅 기능을 사용할 수 있다
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다')
