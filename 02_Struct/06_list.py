# 리스트의 리스트 만들기
#   - 내포된 리스트를 가진 리스트를 초기화해야 하는 경우가 종종있다
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

#   - list.sort()와 sorted() 내장 함수
#       - list.sort()는 사본을 만들지 않고 리스트 내부를 변경해서 정렬한다
#       - sort()메서드는 타깃 객체를 변경하고 새로운 리스트를 생성하지 않았음을 알려주기 위해서 None을 반환한다 -> 관례
#           - 객체를 직접 변경하는 함수나 메서드는 객체가 변경되었고 새로운 객체가 생성 되지 않았을음 호출자에게 알려주기 위해서
#             None을 반환해야 한다
#           - 단점 : chaning을 할수 없다

#       - sorted()는 새로운 리스트를 생성해서 반환한다
#       - 둘다 공통으로 인자 설명
#           - reverse : 참이면 비교연산을 반대로해서 내림차순으로 반환한다. (기본값은 False)
#           - key : 정렬에 사용할 키를 생성하기 위해 각 항목에 적용할 함수를 인수로 받는다
#                   ex) key = str.lower 대소문자를 구분하지 않고 정렬
#                   ex) key = len 문자열의 길이에 따라 문자열을 정렬한다
#                   지정하지 않으면 항목 자체를 비교
fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
print(fruits)
sorted(fruits, reverse=True)
print(fruits)
sorted(fruits, key=len, reverse=True)
print(fruits)

fruits.sort()
print(fruits)

#   - sorted key 사용법
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
a = sorted(student_tuples, key=lambda student: student[2])
print(a)


