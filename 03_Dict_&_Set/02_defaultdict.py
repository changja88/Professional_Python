from collections import defaultdict

#   - defaultdict : 존재하지 않는 키에 대한 또 다른 처리
#       - defaultdict는 인자로 주어진 객체(default-factory)의 기본값을 딕셔너리값의 초깃값으로 지정할수 있다 (숫자, 리스트, 셋등이 가능)
#       - 인자로 주어진 객체에 따라서 기본값이 결정된다 (int 는 0)
#       - default_factory가 설정되어 있지 않으면, 키가 없을 때 흔히 볼수 있는 KeyError 가 발생한다
#       - default_factory는 __getitem()__호출에 대한 기본값을 제공하기 위해 호출되며 다른 메서드는 호출 되지 않는다
#       - 따라서 defaultdict[k] 는 기본 값을 리턴 하지만 defaultdict.get(k)는 None을 반환하다(k값이 저장되어 있지 않은 경우)


a = defaultdict(int)
a['a'] = 3
a['b'] = "abd"
a['c']  # 값을 넣어주지 않으면 0으로 기본 값이 설정된다

print(a.get('d')) # None을 리턴 한다
print(a)



image_upload_type_dict = {'profile': 'profile', 'thumbnail': 'thumbnail'}
print(image_upload_type_dict.get('a'))