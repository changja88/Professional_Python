# 슬라이싱
# [start : end : step]
# 양수 : 연속적인 객체들의 제일 앞에서 부터 0을 시작으로 번호를 매긴다
# 음수 : 연속적인 객체들의 제일 뒤에서부터 -1을 시작으로 번호를 매긴다


# start
#   - 주어진 인수의 index를 포함 한다
# end
#   - 주어진 인수의 index를 포함 하지 않는다
# step
#   - 양수일 경우 오른쪽으로 step 만큼 이동하면서 가져온다
#   - 음수일 경우 왼쪽으로 step 만큼 이동하며서 가져온다


a = [1, 2, 3, 5, 6]

# 전부 가져오기
print(
    a[:]
)

# 거꾸로 전부 가져오기
print(
    a[::-1]
)

# start는 포함하고 end는 포함하지 않는다
print(
    a[0:5]
)

# 맨 마지막 index 가져오기
print(
    a[-1:]
)
