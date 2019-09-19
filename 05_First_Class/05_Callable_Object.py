# 일곱가지 콜라블 객채

# - 호출 연산자인 () 는 사용자 정의 함수 이외의 다른 객체에도 적용할수 있다
# - 호출할 수 있는 객체인지 알아보려면 callable()내장 함수를 사용한다
#       - 파이썬에는 다양한 콜러블형이 존재 하므로 callable()내장 함수를 사용해서 호출할 수 있는 객체인지 판단하는 것이 안전하다

# - 파이썬 데이터 모델 문서는 다음 일곱가지 콜러블을 나열하고 있다
#   - 사용자 정의 함수
#       - def 문이나 람다 표현식으로 생성한다
#   - 내장 함수
#       - len이나 time.strftime()처럼 C언어로 구현된 함수(CPython의 경우)
#   - 내장 메서드
#       - dict.get()처럼 C언어로 구현된 메서드
#   - 메서드
#       - 클래스 본체에 정의된 함수
#   - 클래스
#       - 호출될 때 클래스는 자신의 __new__()메서드를 실행해서 객체를 생성하고
#         __init__ 으로 초기화한후, 최종적으로 호출자에 객체를 반환한다
#         파이썬에는 new 연산자가 없으므로 클래스를 호출하는 것은 함수를 호출하는 것과 동일하다
#         일반적으로 클래스를 호출하면 해당 클래스의 객체가 생성되지만, __new__ 메서드를 오버리읻ㅇ하면
#         다르게 동작할수도 있다
#   - 클래스 객체
#       - 클래스가 __call__메서드를 구현하면 이 클래스의 객체는 함수로 호출될수 있다
#   - 제너레이터 함수
#       - yield 키워드를 사용하는 함수나 메서드, 이 함수가 호출되면 제너레이터 객체를 반환한다
#       - 제너레이터 함수는 여러모로 여타 콜러블과 다르다
#       - 제너레이터 함수는 코루틴으로 사용될수 있다