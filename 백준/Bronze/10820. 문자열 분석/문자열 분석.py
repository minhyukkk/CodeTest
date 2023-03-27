while True:
    try:
        n = input()
        small = 0
        big = 0
        space = 0
        num = 0

        for i in n:
            if 65 <= ord(i) <= 90:
                big+=1
            elif 97 <= ord(i) <= 122:
                small+=1
            elif i == " ":
                space+=1
            else:
                num+=1

        print(small, big , num , space) 
    except EOFError :
        break