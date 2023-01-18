S = str(input())
S_list = []

for i in range(len(S)):
    S_list.append(S[i:]) # 리스트안에 슬라이싱 이용해서 하나씩 자른거를 넣어줌

# S.sort() str은 sort 불가
S_list.sort() # 그래서 list로 바꿔 sort

for i in S_list: # 리스트이기 때문에 이런식의 선언 가능(여러개가 있어서 i당 리스트가 하나씩 들어감)
    print(i)