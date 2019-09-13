# 지능형 리스트(listcomp.)와 제너레이터 표현식(genexp)

# 1. 일반적인 리스트 만드는 방법
symbols = '$%^&*'
codes = []
for symbol in symbols:
    codes.append(symbol)

# 2. 지능형 리스트 사용한 방법
codes1 = [ord(symbol) for symbol in symbols]

# 3. 지능형 리스트와 map()/filter() 비교
# - 지능형 리스트를 사용하면 기능적으로 문제가 있는 파이썬 람다를 억지로 사용하지 않고 구현 할수 있다
beyound_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyound_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

# 3. 지능형 리스트로 데카르트곱 구현하기
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
           for size in sizes]
# 지능형 리스트는 오직 리스트를 만들 뿐이다.
# 다른 종류의 시퀀스를 채우려면 제너레이터 표현식을 사용해야한다


# ListComp를 사용 하면 list가 반환이 된다 !!!
print(type(tshirts))
