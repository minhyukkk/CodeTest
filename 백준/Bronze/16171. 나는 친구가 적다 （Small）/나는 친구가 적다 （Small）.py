s = str(input())
want = str(input())

result = []
for i in s:
    if ord(i) >= 65 and ord(i) < 91: # 대문자 판별
        result.append(i)
    
    if ord(i) >= 97 and ord(i) < 123: # 소문자 판별
        result.append(i)

result = ''.join(result) # ['', '', '', '', ''] 이런식으로 정리된 리스트를 '  ' 이렇게 바꿔줌

if want in result:
    print(1)
else :
    print(0)