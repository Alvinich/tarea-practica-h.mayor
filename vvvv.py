n1=int(input("escriba un numero"))
n2=int(input("escriba otro numero"))
suma= n1 + n2
multiplicacion= n1 * n2
print("la suma es",suma)
print("la multiplicaion es",multiplicacion)
if n2!=0:
    residuo=n1%n2
    print("el residuo es",residuo)
else:
    print("no se puede calcular")