# testar com var =3, 15, 20, 80 e 120

var = int(input("Digite um número: "))
if var >=20:
    print("Seu número é igual ou maior que 20")
    if var <= 100:
        print("É menor ou igual a 100")
    else:
        print("É maior que 100")
else:
    if var < 10 :
        print("Seu número é menor que 10")
    else: 
        print("Seu número é maior que 10 e menor que 20")    