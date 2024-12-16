valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])
a1 = C *A / 2
a2 = 3.14159 * C * C
a3 = (A + B) * C / 2
a4 = B * B
a5 = A * B
print("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f" %(a1, a2, a3, a4, a5))
