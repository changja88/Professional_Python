"""
메타클래스 기본지식
"""
"""
- 메타클래스는 일종의 클래스 팩토리다 (다만 형태가 클래스이다)
- 파이썬 객체 모델을 생각해보면, 클래스도 객체이므로, 각 클래스는 다른 어떤 클래스의 객체여야 한다
- 기본적으로 파이썬 클래스는 type의 객체다
- 즉, type은 대부분의 내장된 클래스와 사용자 정의 클래스에 대한 메타클래스이

- object와 type 클래스는 독특한 관계를 맺고있다. object는 type의 객체며, type은 object의 서브클래스다
- 이 관계는 '마술'과도 같아서 파이썬으로는 표현할 수 없다
- 두 클래스 모두 다른 클래스를 정의하기 전에 존재해야 하기 때문이다

- 모두다 궁극적으로 type의 객체지만, 메타클래스만 type의 서브클래스이다
- 메타클래스는 type으로부터 클래스 생성 능력을 상속한다 
"""