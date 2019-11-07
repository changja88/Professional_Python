

"""
내장 자료형 상속과 다중 상속
- 내장 자료형 상속의 위험성
- 다중 상속과 메서드 결정 순서
"""
"""
- 내장 자료형의 상속은 까다롭다
- 사용자가 정의한 오버라이드된 메서드를 무시하므로 직접 상속하지마라라(c언어로 구현된 내장 자료형)
    - 내장형 자료형 말고 상속을 위해서 만들어 놓은 클래스를 상속해서 사용해라
    - dict -> collections.UserDict를 상속해서 사용해서 사용해라
"""
