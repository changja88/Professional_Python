"""
Contextlib 유틸리티
"""
"""
closing 
    - close()메서드는 제공하지만 __enter__, __exit__ 프로토콜을 구현하지 않는 개체로부터 콘텍스트 관리자를 생성하는 함수
suppress
    - 지정한 예외를 임시로 무시하는 콘텍스트 관리자
@contextmanager
    - 클래스를 생성하고 프로토콜을 구현하는 대신, 간단한 제너레이터 함수로부터 콘텍스트 관리자를 생성할 수 있게 해주는 데커레이터
ContextDecorator
    - 콘텍스트 관리자를 함수 데커레이터로도 사용할 수 있게 해주는 기반 클래스
ExitStack
    - 여러 콘텍스트 관리자를 입력할 수 있게 해주는 콘텍스트 관리자. With블럭이 끝나면 ExitStack은 누적된 콘텍스트 관리자들의
      __exit__메서드를 LIFO순서로 호출한다. 예를 들어 임의의 파일 리스테 있는 파일을 한꺼번에 여는 경우처럼, with블록
      안에 들어가기 전에 얼마나 많은 콘텍스트 관리자가 필요한지 사전에 알 수 없을 때 이 클래스를 사용해라
"""

"""
@contextmanager사용하기
"""
"""
- @contextmanager데커레이터는 콘텍스트 관리자를 생성할 때 작성하는 틀에 박힌 코드를 줄여준다
- __enter__와 __exit__메서드를 가진 클래스 전체를 작성하는 대신 __enter__메서드가 반환할 것을 생성하는 yield문 
  하나를 가진 제너레이터만 구현하면 된다
- @contextmanager로 데커레이트된 제너레이터에서 yield는 함수 본체를 두 부분으로 나누기 위해 사용된다
  yield문 앞에 있는 모든 코드는 with 블록 앞에서 인터프리터가 __enter__를 호출할 때 실행되고, yield문 뒤에 있는
  코드는 블록의 마지막에서 __exit__가 호출될 때 실행된다
"""
import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write


with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)

print(what)
"""
즉, @contextlib.contextmanager데커레이터는 데커레이트된 함수를 __enter__와 __exit__메서드를 구현하는 클래스안에 넣을 뿐이다
- __enter__안에서 벌어지는 일
    - 제너레이터 함수를 호출해서 제너레이터 객체를 보관한다(gen 이라고 부르자)
    - next(gen)을 호출해서 yield키워드 앞까지 실행한다
    - next(gen)이 생성한 값을 반환해서, 이 값이 as 절의 타깃 변수에 바인딩되게 한다
- __exit__안에서 벌어지는 일
    - exit_type예외가 전달되었는지 확인한다. 만일 그렇다면 제너레이터 함수 본체 안에 있는 yield행에서 gen,throw(exception)
      을 실행해서 예외를 발생시킨다
    - 그렇지 않다면 next(gen)을 호출해서 제너레이터 함수 본체 안의 yield다음의 코드를 계속 실행한

- 다시 말하면 yield 전까지를 __enter__에 보내주고, yield이후를 __exit__에 보내준다 
"""

"""
- 위 코드의 문제점
    - with 블럭 안에서 예외가 발생하면 파이선 인터프리터가 이 예외를 잡고, looking_glass()안에 있는 yield표현식에서
      다시 예외를 발생시킨다. 그러나 그곳에는 예외 처리 코드가 없어서 looking_glass함수는 원래의 sys.stdout.wirte()
      메서드를 복원하지 않고 중단하므로, 시스템이 불안정한 상태로 남게 된다
"""


@contextlib.contextmanager
def looking_glass2():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
"""
- 즉, @contextmanager를 사용할 때는 어쩔 수 없이 yield문 주변을 try/finally나 with블럭으로 둘러싸야 한다
  콘텍스트 관리자의 사용자가 자신의 with블럭 안에서 어떤 일을 할지 모르기 때문이다
"""

