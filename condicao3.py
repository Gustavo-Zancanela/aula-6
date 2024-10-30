# testar com var = 10, 15, 35, 55, 75, 80, 90 e 120

var = int(input("Digite um número: "))
if var <= 10:
    print("Seu número é menor ou igual a 10")
elif var <=20:
    print("Seu número é maior qu 10 e menor ou igual a 20")
elif var <=40:
    print("Seu número é maior qu 20 e menor ou igual a 40")
elif var <=60:
    print("Seu número é maior qu 40 e menor ou igual a 60")
elif var <=80:
    print("Seu número é maior qu 60 e menor ou igual a 80")
else:
    print("Seu número é maior que 80")