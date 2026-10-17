notafinal= float(input("ingrese la nota"))
if notafinal<0 or notafinal>100:
    print("nota no valida")
elif notafinal<=50:
    print("reprovado con",notafinal)
else:
    print("aprovado con",notafinal)