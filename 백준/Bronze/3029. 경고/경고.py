h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))

t1 = h1*60*60 + m1*60 + s1 # 초로 변환
t2 = h2*60*60 + m2*60 + s2

if t2 > t1:
    t = t2 - t1
else:
    t = 86400 - (t1-t2) # 24시간을 초로 변환 = 86400

h = t // 60 // 60
m = t // 60 % 60
s = t % 60
#초로 변환한 시간을 각 별로 다시 계산하는 식

print("%02d:%02d:%02d" %(h,m,s))