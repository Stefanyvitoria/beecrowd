N = int(input())
h = 0
m = 0
s = 0
while N >= 3600:
        N -= 3600
        h += 1
while N >= 60:
        N -= 60
        m += 1
while N >= 1:
        N-= 1
        s += 1
print("{}:{}:{}".format(h,m,s))