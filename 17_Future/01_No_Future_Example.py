"""
Future를 이용한 동시성
"""
"""
- 비동기 작업의 실행을 나타내는 객체인 Future
- Future가 asyncio패키지의 기반이 된다
- 동시성이 하나도 없는 순차적으로 실행하는 예제
"""

import os
import time
import sys
import requests

POP20_CC = ('CN IN US ID BR PK NG RU JP MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = '/Users/rayleigh/Desktop/test/'

print(os.path.join(DEST_DIR))


def save_flag(img, filename):
    with open(DEST_DIR + filename, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    url = '{}/{cc}/{cc}.git'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url=url)
    return resp.content


def show(text):
    print(text, end='  ')
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')

    return len(cc_list)


def main():
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


main()
