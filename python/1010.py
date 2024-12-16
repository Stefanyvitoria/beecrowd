peca1 = input().split(" ")
peca2 = input().split(" ")

c1 = int(peca1[0])
c2 = int(peca2[0])
q1 = int(peca1[1])
q2 = int(peca2[1])
v1 = float(peca1[2])
v2 = float(peca2[2])

vp = q1 * v1 + q2 * v2
print("VALOR A PAGAR: R$ %.2f" %vp)
