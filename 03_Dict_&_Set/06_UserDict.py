# UserDict
#   - dict 보다는 UserDict를 상속해서 매핑형을 만드는 것이 쉽다
#   - 매핍에 추가한 키를 문자열로 저장하기 위해 StrKeyDict0을 확장했던 것 처럼 userDict의 값을 평가 할 수 있다
#   - 내장형에서는 아무런 문제없이 상속할 수 있는 메서드들을 오버라이드해야 하는 구현의 특성 때문에 dict보다는  UserDict를 상속 하는 것이 좋다
#   - UserDict는 dict를 상ㅅ혹하지 않고 내부에 실제 항목을 담고 있는 data라고 하는 dict객체를 갖고 있다
#     이렇게 구현함으로써 __setitem__ 등의 특수 메서드를 구현할 때 방생하는 원치 않는 재귀적 호출을 피할수 있으며,
#     __continas__메서드를 간단히 구현할 수 있다

import collections


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

#   - UserDict 클래스가 MutableMapping을 상속하므로 StrKeyDict는 결국 UserDict, MutableMapping, 또는 Mapping
#     을 상속하므로 StrKeyDict는 결국 UserDict, MutableMapping 또는 Mapping을 상속하게 되어 매핑의 모든 기능을 가지게 된다
#     Mapping 은 추상 베이스 클래스(ABC)임에도 불구하고 유용한 구상 메서드를 다수 제공한다
#   - Mapping을 상속함으로써 생기는 유용한 메서드
#       - MutableMapping.update()
#           - 직접 호출할 수도 있지만, 다른 매핍이나 쌍의 반복형 및 키워드 인수에서 객체를 로딩하기 위해 __init__에 의해 사용될 수도 있다
#           - self[키] = 값 구문을 사용하므로 결국 서브클래스에서 구현한 __setitem__메서드를 호출 하게 된다
#       - Mapping.get()
#           - __getitem__()과 일치하는 결과를 가져오기 위해서 get() 메서드를 직접 구현해야 했지만, 어쩌라고
