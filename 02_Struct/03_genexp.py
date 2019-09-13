# 제너레이터 표현식
symbols = '!@#$%^'
tuple(ord(symbol) for symbol in symbols)
# 제너레이터 표현식이 함수에 보내는 단 하나의 인수라며 ㄴ괄호 안에 또 괄호를 넣을 필요는 없다
import array

array.array('I', (ord(symbol) for symbol in symbols))
# 배열 생성자는 인수를 두개 받으므로 제너레이터 표현식 앞뒤에 반드시 괄호를 넣어야 한다
# array.array
#   - 기본적으로 array.array는 동일한 타입만을 인수로 같기 위해서이다
#   - 첫번째 인수는 타입을 지정한다
#   - I -> unsigned int


# 제너레이터 표현식으로 데카트트 곱
colors = ['black', 'white']
sizes = ['S', 'M', "L"]
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)





# GenExp을 사용하면 반환 타입이 genexp 이다
#   - 리스트를 통째로 만들지 않고 반복자 프로토콜을 이용해서 항목을 하나씩 생성한다 ! -> 메모리를 더 적게 사용한다
tshirt = ((color, size) for color in colors for size in sizes)
print(type(tshirt))

