"""
concurrent.futures 로 내려 받기
"""
import sys
import time

import requests

"""
- concurrent.futures 패키지의 가장 큰 특징은 ThreadPoolExecutor와 ProcessPoolExecutor클래스 인데,
  이 클래스들은 콜러블 객체를 서로 다른 쓰레드나 프로세스에서 실행할 수 있게 해주는 인터페이스를 구현한다
- 이 클래스들은 작업자 스레드나 작업자 프로세스를 관리하는 풀과 실해할 작업을 담은 큐를 가지고 있다.
  그러나 아주 고수준의 인터페이스를 구현하고 있어서 국기를 내려받는 간단한 프로그램을 구현할 때는 내부의 작동 과정을 알 필요가 없다
"""

from concurrent import futures

POP20_CC = ('CN IN US ID BR PK NG RU JP MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = '/Users/rayleigh/Desktop/test/'


def get_flag(cc):
    url = '{}/{cc}/{cc}.git'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url=url)
    return resp.content


def main():
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


def show(text):
    print(text, end='  ')
    sys.stdout.flush()


def save_flag(img, filename):
    with open(DEST_DIR + filename, 'wb') as fp:
        fp.write(img)


MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))  # 작업자 수 결정
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
        # map -> 여러 스레드에 의해 download_one이 동시에 호출되는 것을 제외하면 내장 map과 비슷하다
        # map -> 사용자에게 보이지 않도록 내부에서 Future객체를 사용하는 예
    return len(list(res))


main()
