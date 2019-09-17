# 불변 매핑
# - MappingProxyType
#       - 원래 매핑의 동적인 뷰를 제공하지만 읽기 전용의 mappingproxy를 반환한다
#       - 따라서 원래 매핑을 변경하면 mappingporxy에 반영이 되지만 mappingproxy를 직접 변경할 수는 없다


from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d)

# d_proxy[2] = 'X' # 변경 할수 없다
# print(d_proxy)

d[2] = 'B' # 동적인 d_proxy는 d에 대한 변경을 바로 반영한다
print(d_proxy)
