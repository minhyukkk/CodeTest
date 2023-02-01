
while 1:
    s = input()
    stack = []

    if s == '.':
        break

    for j in s:
        if j == '(' or j == '[':
            stack.append(j)

        elif j == ')':
            if len(stack) != 0 and stack[-1] == '(': # 길이 0이면 어차피 대칭 x , stack에서 하나 줄였을 때도 매핑 된다면
                stack.pop() # pop해줘서 그 문자 없애줌
            else:
                stack.append(j)
                break # 아니면 stack 넣을 필요없이 안되기 때문에 바로 break 해줌
            ######## 바로 break 해주려고 했으나 처음에 ), ]가 처음부터 나오면 바로 break가 되어서 stack의 len은 0이 됨 그래서 답이 yes가 나오기때문에 꼭 append 필수

        elif j == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(j)
                break
    
    if len(stack) == 0:
        print('yes')
    else:
        print('no')