"""
인터페이스 : 프로토콜에서 ABC 까지
- 덕 타이핑의 상징인 동적 프로토콜에서부터 인터페이스를 명시하고 구현이 인터페이스에 따르는지 검증하는
  추상 베이스 클래스(abstract base class, ABC)에 이르기까지 다양한 곳에서 인터페이스가 사용된다
- 기본적으로 파이썬에는 interface라는 키워드가 없지만, ABC에 상관없이 모든 클래스는 인터페이스를 가지고 있다
  클래스가 상속하거나 구현한 공개 속성(메서드나 데이터속성)들의 집합이 인터페이스다
  __getitem__, __add__같은 특별 메서드도 포함한다
  보호된 속성과 비공개 속성은 인터페이스에 속하지 않는다고 정의되어 있다. (관례를 어기는 것은 좋지 않다)
  공개 데이터 속성을 객체의 인터페이스로 사용하는 것은 나쁘지 않다
"""
"""
- 어떤 역할을 완수하기 위한 메서드 집합으로서의 인터페이스를 스몰토크에서는 '프로토콜'이라고 불렀다
- 프로토콜은 인터페이스지만 비공식적이다. 즉, 문서와 관례에 따라 정의되지만, 공식 인터페이스처럼 강제할 수 없다
"""


