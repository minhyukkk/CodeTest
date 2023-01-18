t = int(input())

n = []
for i in range(t):
    n.append(input()) # sort나 이러한 것들을 하기 위해서 append를 통해서 입력 받음

set_n = set(n) # 중복 값을 제거하기 위한 set함수 사용
n = list(set_n) # sort하기 위해 다시 list로 변환

n.sort()
n.sort(key = len) # 하위 조건이 있다면 하위 조건을 실행 후 상위 조건을 실행하야 원하는 값이 나옴
# key = len을 통해 길이에 따라 정렬

for i in n:
    print(i)