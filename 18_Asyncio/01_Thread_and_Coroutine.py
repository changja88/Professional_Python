"""
asyncio를 이용한 동시성
"""
"""
동시성(concurrent)과 병렬성(parallel)의 차이
- 둘의 차이점을 알기전에 순차적(sequential)을 알면 이해하기 쉬움
- 순차적은 하나끝나면 다른 하나를 시작
- 동시성은 작업을 왔다 갔다 하는 것 
    - 즉 싱글 코어에서 여러 쓰레드로 작업을 하는 것
- 병렬성은 복수개의 작업을 동시에 실행 하는것
    - 코어 하나가 작업 하나를 담당
    - 코어가 4개면 4개까지 병렬로 처리 할 수 있다 
    
- 병렬처리보다는 동시성이 더 낫다
"""

"""
스레드와 코루틴 비교
- 쓰레드 및 GIL에 대해 설명
"""
import threading
import itertools
import time
import sys

class Signal:
    go = True

