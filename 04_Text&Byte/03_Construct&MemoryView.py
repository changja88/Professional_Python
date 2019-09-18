# 구조체와 메모리 뷰
# - struct 모듈은 패킹된 바이트를 다양한 형의 필드로 구성된 튜플로 분석하고,
#   반대로 튜플을 패킹된 바이트로 변환하는 함수를 제공한다
# - struct는 bytes, bytearray, memoryview 객체와 함계 사용된다

import struct

fmt = '<3s3sHH'
with open('/Users/rayleigh/Desktop/download.jpg', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
bytes(header)

a = struct.unpack(fmt, header)
print(a)

del header
del img
