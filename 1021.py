valor = (input())
n = valor.split(".")
cedula = int(n[0])
moeda = int(n[1])
nota100 = 0
while cedula >= 100:
    nota100 +=1
    cedula -= 100
print("NOTAS:\n{} nota(s) de R$ 100.00".format(nota100))
nota50 = 0
while cedula >= 50:
    nota50 +=1
    cedula -= 50
print("{} nota(s) de R$ 50.00".format(nota50))
nota20 = 0
while cedula >= 20:
    nota20 +=1
    cedula -= 20
print("{} nota(s) de R$ 20.00".format(nota20))
nota10 = 0
while cedula >= 10:
    nota10 +=1
    cedula -= 10
print("{} nota(s) de R$ 10.00".format(nota10))
nota5 = 0
while cedula >= 5:
    nota5 +=1
    cedula -= 5
print("{} nota(s) de R$ 5.00".format(nota5))
nota2 = 0
while cedula >= 2:
    nota2 +=1
    cedula -= 2
print("{} nota(s) de R$ 2.00".format(nota2))
print("MOEDAS:")
moeda1 = 0
while cedula >= 1:
    moeda1 += 1
    cedula -= 1
print("{} moeda(s) de R$ 1.00".format(moeda1))


moeda50 = 0
while moeda >= 50:
    moeda50 += 1
    moeda -= 50
print("{} moeda(s) de R$ 0.50".format(moeda50))
moeda25 = 0
while moeda >= 25:
    moeda25 += 1
    moeda -= 25
print("{} moeda(s) de R$ 0.25".format(moeda25))
moeda10 = 0
while moeda >= 10:
    moeda10 += 1
    moeda -= 10
print("{} moeda(s) de R$ 0.10".format(moeda10))
moeda05 = 0
while moeda >= 5:
    moeda05 += 1
    moeda -= 5 
print("{} moeda(s) de R$ 0.05".format(moeda05))
moeda01 = 0
while moeda >= 1:
    moeda01 += 1
    moeda -= 1
print("{} moeda(s) de R$ 0.01".format(moeda01))
