# 바이트에 대한 기본 지식
# - 이진 시퀀스를 위해 사용되는 내장형 자료형은 bytes와 bytearray, 두가지가 있다.
# - bytes는 파이썬3에서 소개된 불변형이고, bytearray는 파이썬 2.6에 추가된 가변형이다
# - bytes와 bytearray 에 들어 있는 각 항목은 0에서 255 사이의 정수로, 파이썬2의 str에 들어있는 문자 하나로 구성된 문자열과는 다르다
# - 그러나 이진 시퀀스를 슬라이싱하면 언제나 동일한 자료형의 이진 시퀀스가 만들어지며, 슬라이스 길이가 1일 때도 만찬가지다
# - 어쩌라고
cafe = bytes('café', encoding='utf_8')
print(cafe)

print(
    cafe[0]
)

print(
    cafe[:1]
)

cafe_arr = bytearray(cafe)
print(cafe_arr)

print(
    cafe_arr[-1:]
)

