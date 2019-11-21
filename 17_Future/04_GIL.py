"""
블로킹 I/O와 GIL(Global Interpreter Lock)
"""
"""
- Cpython 인터프리터는 내부적으로 스레드 안전하지 않으므로, 전역 인터피리터 락(GIL)을 가지고 있다
  GIL은 한번에 한 스레드만 파이썬 바이트 코드를 실행하도록 제한한다
  그렇기 때문에 단일 파이썬 프로세스가 동시에 다중 CPU코어를 사용할 수 없다
  
- 블로킹 입출력을 실행하는 모든 표준 라이브러리 함수는 OS에서 결과를 기다리는 동안 GIL을 헤제한다
- 즉, 입출력 위주의 작업을 실행하는 파이썬 프로그램은 파이썬으로 구현하더라도 쓰레드를 이용함으로써 이득을 볼 수 있다
- 파이썬 스레드가 네트워크로부터의 응답을 기다리는 동안, 블로킹된 입출력 함수가 GIL을 헤제함으로써 다른 스레드가 실행될 수 있다
"""
