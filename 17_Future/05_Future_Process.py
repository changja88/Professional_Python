"""
concurrent.futures로 프로세스 실행하기
"""
"""
- ProcessPoolExecutor는 GIL을 회하므로 '계산' 위주의 작업을 수행해야 하는 경우 가용한 CPU를 모두 사용한다
- ProcessPoolExecutor와 ThreadPoolExecutor는 모두 범용 executor인터페이스를 구현하므로, concurrnt.future를
  사용하는 경우에는 스레드 기반의 프로그램을 프로세스 기반의 프로그램으로 쉽게 변환할 수 있다
- 국기를 내려받는 프로그램처럼 입출력 위주의 작업에서는 ProcessPoolExecutor를 사용해도 도움이 안된다
"""
