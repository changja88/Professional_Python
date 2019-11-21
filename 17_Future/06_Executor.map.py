"""
Executor.map()실험
"""
"""
- Executor.map() 메서드를 시용하면 여러 콜러블을 아주 간단히 동시에 실행할 수 있다
"""
from time import sleep, strftime
from concurrent import futures


def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s....'
    display(msg.format('\t' * n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t' * n, n))
    return n * 10


def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=1)
    results = executor.map(loiter, range(5))
    display('results:', results)
    display('Wating for individual results:')
    for i, result in enumerate(results):
        display('result {}: {}'.format(i, result))


main()
