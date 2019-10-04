# 함수 애너테이션
# - 파이썬3는 함수의 매개변수와 반환값에 메타테이터를 추가할 수 있는 구문을 제공한다 (첫줄만 보면된다)
def clip(text:'hello', max_len: 'int>0' = 80) -> str:
    """
    max_len 앞이나 뒤의 마지막 공백에서 잘라낸 텍스트를 반환한다
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind('', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind('', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)
    return text[:end].rstrip()
# - 함수 선언에서 각 매개변수에 콜론 뒤에 애너테이션 표현식을 추가할 수 있다
# - 기본값이 있을때, 애너테이션은 인수명과 등호(=) 사이에 들어간다
# - 반환값에 애너테이션을 추가하려면 매개변수를 닫는 괄호와 함수 선언의 제일 뒤에 오는 콜론 사이에 -> 기화화 표현식을 추가한다
# - 표현식은 어떤 자료형도 될수 있다, int,str 과 같은 클래스 혹은 위 예제 철엄 'int>0' 과 같은 문자열이 가장 널리 사용된다
# - 애너테이션은 전현 처리하지 않으며, 단지 함수 객체 안의 dict형 __annotations__속성에 저장될 뿐이다
print(clip.__annotations__)
# - 애너테이션은 파이썬 인터프러터에게는 아무런 의미가 없다 단지 메타데이터일 뿐이다