"""
이것 다음에 저것: if 문 이외에서의 else 블록
"""
"""
- 다들 잘 모르겠지만, else절은 if문뿐만아니라 for, while, try문에서도 사용할 수 있다.
for -> for 루프가 완전히 실행된 후에(break문으로 중간에 멈추지 않고)else 블럭이 실행된다 (then에 더 가깝다)
while -> 조건식이 거짓이 되어 while 루프를 빠져나온 후에(break 문으로 중간이 멈추지 않고) else 블록이 실행 된다
try -> try블록에서 예외가 발생하지 않을 때만 else 블럭이 실행된다, 그리고 else 블록에서 발생한 예외는
       else 블럭 앞에 오는 except 블록에서 처리되지 않는다

즉, 예외, return, break, continue문이 복합문의 주요 블록을 빠져나오게 만들면 else 블럭은 실행되지 않는다
"""
# 루프에서의 사용 예
for item in my_list:
    if item.flavor = 'banana':
        break
else:
    raise ValueError("Not banana flavor found!")

# else문을 안썼을 때
try:
    dangerouse_call()
    after_call()
except OSError:
    log('OSError...')
# else문을 사용했을 때 -> try문에는 예외가 발생할수 있는 코드만 넣는 것이 좋기 때문에 이쪽이 더 좋은 코드이다
try:
    dangerouse_call()
except OSError:
    log('OSError...')
else:
    after_call()


