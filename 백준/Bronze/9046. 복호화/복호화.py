t = int(input())

for i in range(t):
    a = input()

    max = ""
    max_count = 0

    for j in range(ord('a'), ord('z')+1):
        current_count = a.count(chr(j)) # count함수를 사용해 j의 갯수를 current_count에 넣음

        if current_count > max_count:
            max = chr(j)
            max_count = current_count

        elif current_count == max_count:
            max = "?"
        else:
            continue
    
    print(max)