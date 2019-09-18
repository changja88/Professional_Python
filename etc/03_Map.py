# Map
# - map(f, iterable)은 함수와 반복가능한 자료형을 입력으로 받는다
# - map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다

# Map 사용 전
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result


result = two_times([1, 2, 3, 4])
print(result)


# Map 사용
def two_times(x):
    return x * 2


a = list(map(two_times, [1, 2, 3, 4]))
print(a)
