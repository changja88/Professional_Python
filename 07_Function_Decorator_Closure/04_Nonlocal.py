# Nonlocal

# 전체 이력을 유지하지 않고 이동 평균을 계산하는 잘못된 고위 함수
def amke_averager1():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager


# - count가 수치형이거나 어떤 가변형일 때 count += 1 문이 실제로는 count = count + 1을 의미하기 때문에 문제가 발생한다
#   따라서 averager() 본체 안에서 count 변수에 할당하고 있으므로 count를 지역 변수로 만든다 (total도 마찬가지)
# - 숫자, 문자열, 튜플 등 불변형은 읽을 수만 있고 값은 갱신 할 수 없다

# 수정 버젼
def amke_averager2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


# - nonlocal을 선언하면 함수 안에서 변수에 새로운 값을 할당하더라도 그 변수는 자유 변수임을 나타낸다
# - 새로운 값을 nonloal 변수에 할당하면 클로저에 저장된 바인딩이 변경된다

# 이건 왜 될까?
def make_averager3():
    series = []  # 지역 변수 a

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager
# - series 변수에 할당하지 않기 때문에 이런 문제가 생기지 않았다. 단지 series.append()를 호출한 후
#   sum() 과 len()을 호출 했을 뿐이다 (리스트가 가변형 이라는 사실을 이용)
