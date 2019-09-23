# 클로저
# - 클로저를 익명함수와 혼동하는 경우가 있다
# - 클로저는 함수 본체에서 정의하지 않고 참조하는 비전역 변수를 포함함 확장 범위를 가진 함수다
# - 함수가 익명 함수인지 여부는 중요하지 않다. 함수 본체 외부에 정의된 비전역 변수에 접근 할 수 있다는 것이 중요하다

# avg() 함수가 점차 증가하는 일련의 값의 평균을 계산 한다고 가정
# avg(10) -> 10.0
# avg(11) -> 10.5
# avg(12) -> 11.0
# - avg()는 어떻게 이전 값을 기억하고 있는 걸까?

# 이동 평균을 계산하는 클래스
class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))


# 이동 평균을 계산하는 고위 함수
def make_averager():
    series = []  # 지역 변수 a

    def averager(new_value):
        series.append(new_value)  # 여기에서 series는 자유 변수 이다 -> 지역 볌위에 바인딩되어 있지 않은 변수
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()  # 함수가 호출되었음으로 지역변수 a도 사라진다
print()
print(avg(10))
print(avg(11))
print(avg(12))

print()
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)  # 자유 변수 확인 가능
print(avg.__closure__)  # 여기에 저장된다
print(avg.__closure__[0].cell_contents)  # 저장된 값도 확인 가능 하다
# - 정리하면, 클로저는 함수를 정의할 때 재하던 자유 변수에 대한 바인딩을 유지하는 함수다
#   따라서 함수를 정의하는 범위가 사라진 후에 함수를 호출해도 자유 변수에 접근 할 수 있다
