# 슬라이싱
#   - list, tuple, str 그리고 모든 시퀀스형은 슬라이싱 연산을 지원한다

#   - 슬라이스와 범위 지정시에 마지막 항목이 포함되지 않는 이유
#       - 인덱스가 0부터 시작하는 관례를 이용하기 위해서
l = [10, 20, 30, 40, 50, 60]
print(l[:2])
print(l[2:])
print(l[3:5])  # 앞은 포함이고 뒤는 제외이다

#   - 슬라이스 객체
s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])
#       - [a:b:c]는 결국 slice(a,b,c) 객체를 생성한다
#       - 슬라이스를 객체로 사용하면 유용하다
#           - 어떤 문자열을 파싱해야 하는 경우 슬라이싱객체에 이름을 지어 놓으면 좋다
SKU = slice(0, 6)
DESCRIPTIOn = slice(6, 40)
UNIT_PRICE = slice(52, 55)
ITEM_TOTAL = slice(55, None)

# 다차원 슬라이싱과 생략 기호
#   - 패스

# 슬라이스에 할당하기
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
# l[2:5] = 100  # 범위를 지정했음으로 iterable을 할당 해야함
l[2:5] = [100]  # iterable을 넣어줘도 범위보다 짧으면 그냥 맞는곳 까지만 알아서 들어감
print(l)

