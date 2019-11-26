"""
동적 속성과 프로퍼티
- 프로퍼티를 통해 공개 데이터 속성을 클래스의 공개 인터페이스로 노출시키는 것은 완전히 안전하며,
  실제로 그렇게 하도록 권장할 수 있다는 것이 프로퍼티의 가장 중요한 점이다
"""
"""
- 파이썬에서는 데이터 속성과 메서드를 통틀어 속성이라고 한다
- 메서드는 단지 호출할 수 있는 속성일 뿐이다
- 데이터 속성과 메스드 외에도 프로퍼티를 정의할 수 있따
- 프로퍼터리를 사용하면 클래스 인터페이스를 변경하지 않고도 공개 데이터 속성을 접근자 메서드(게터, 세터)로 대체할 수 있다
  - 통일된 접근 원칙에도 부합한다 
  - 모듈이 제공하는 모든 서비스는 통일된 표기법을 이용해서 접근할 수 있어야 한다. 통일된 표기법은 저장소를 이용해서 구현하거나
    계산을 통해 구현하는 경우에도 모두 동일하게 적용된다(통일된 접근 원칙) 
    
- 프로퍼티 외에도 파이썬은 속성에 대한 접근을 제어하고 동적 속성을 구현할 수 있는 풍부한 API를 제공한다
- 파이썬 인터프리터는 obj.attr과 같은 점 표기법으로 표현된 속성에 대한 접근을
  __getattr__과 __setattr__등 특별 메서드를 호출해서 평가한다. 
"""

"""
동적 속성을 이용한 데이터 랭글링
"""
from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = '/Users/rayleigh/Desktop/Professional_Python/19_Meta_Programing/data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)

        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)


feed = load()
sorted(feed['Schedule'].keys())
for key, value in sorted(feed['Schedule'].items()):
    print('{:3} {}'.format(len(value), key))

from collections import abc


class FrozenJSON:
    """
    점 표기법을 이용해서 JSON과 유사한 객체를 순회하는 읽기전용 퍼사드 클래스
    """

    def __int__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


raw_feed = load()
feed = FrozenJSON(raw_feed)
sorted(feed.Schedule.keys()) # __getattr__때문에 가능하
for key, value in sorted(feed.Schedule.items()):
    print('{:3} {}'.format(len(value), key))

"""
- __getattr__ 특별 메소드는 속성을 가져오기 위한 일반적인 과정이 실패 할 때(즉, 지명한 속성을 객체, 클래스, 슈퍼클래스에서
  찾지 못할때)만 인터프리터에서 호출한다
"""