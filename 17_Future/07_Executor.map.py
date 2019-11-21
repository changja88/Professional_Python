from concurrent import futures
from time import sleep, strftime

"""
executor.map 알아보기
- worker 갯수에 따른 호출 방식
    - worker의 갯수에 따라 help의 print(*args)가 다르게 호출된다
    - 워커의 갯수만큼 help가 한번에 호출된다
"""


def help(*args):
    print(*args)


def main():
    executor = futures.ThreadPoolExecutor(max_workers=1)  # worker갯수 바꿔 가면서 출력해보면 된다
    results = executor.map(help, range(3))


main()
sleep(1)
"""
- executor의 결과값 알아보기
    - 인덱스와, 함수 실행 결과 두개가 들어 있다 
"""


def help(*args):
    sleep(1)
    print('aaa')
    return 'a'


def main():
    print()
    executor = futures.ThreadPoolExecutor(max_workers=2)  # worker갯수 바꿔 가면서 출력해보면 된다
    results = executor.map(help, range(3))
    for i, result in enumerate(results):
        print(i, result)


main()
