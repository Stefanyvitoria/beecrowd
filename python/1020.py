dias = int(input())
d = 0
m = 0
a = 0
while True:
    if dias >= 365:
        a +=1
        dias -= 365
    if dias >= 30:
        m += 1
        dias -=30
    else:
        break
print("{} ano(s)".format(a))
print("{} mes(es)".format(m))
print("{} dia(s)".format(dias))
