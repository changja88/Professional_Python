"""
콘텍스트 관리자와 with 블럭
"""
"""
- open -> 콘텍스트 관리
- 반복자가 for문을 제어하기 위해 존재하는 것과 마찬가지로, 콘텍스트 관리자 객체는 with문을 제어하기 위해존재한다
- with문은 try/finally 패턴을 단순화하기 위해 설계되었다
  일반적으로 finally절 안에 있는 코드는 중요한 리소스를 해재하거나 임시로 변경된 상태를 복원하기 위해 사용된다
- 콘텍스트 관리자 프로토콜은 __enter__, __exit__메서드로 구성된다
  with문이 시작될 때 콘텍스트 관리자 객체의 __enter__메서드가 호울된다
  이 메서드는 with블럭의 끝에서 finally 절의 역할을 수행한다
"""
# with open('mirro.py')as fp:
# src = fp.read(60)

"""
with -> 콘텍스트 관리자 객체는 with문 뒤의 표현식을 평가한 결과지만, as절에 있는 타깃 변수의 값은 콘텍스트
- open 함수가 TextIOWrapper객체를 반환하고, 이 객체의 __enter__메서드는 self를 반환했을 뿐이다
  그러나 __enter__메서드는 콘텍스트 관리자 대신 다른 객체를 반환할 수도 있다
- 제어 흐름이 with문을 빠져나온 후에는 __enter__메서드가 반환한 객체가 아니라 콘텍스트 관리자 객체 __exit__메서드가 호출된다
"""


class LookingGlass:
    def __enter__(self):
        import sys
        self.original_wirte = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_wirte(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        """
        :param exc_type: ZeroDivisionError등의 예외 클래스
        :param exc_value: 예외 객체, 예외 메시지 등 exception() 생성자에 전될단 인수는 exc_value.args속성을 이용해서 볼수 있다
        :param traceback: traceback 객체
        :return:
        """
        import sys
        sys.stdout.write = self.original_wirte
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True


with LookingGlass()as what:
    print('Alice, Kitty and Snowdrop')
    print(what)

print(what)
print('back to normal')

"""
예제
"""


class Original:
    abc = '123'

    def __enter__(self):
        print('__enter__')
        self.abc = 'abc'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        self.abc = 'def'


with Original() as ori:
    print(ori.abc)

print(ori.abc)
