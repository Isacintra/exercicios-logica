nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 16:
    print(nome, "não vota")

elif idade >= 16 and idade < 18:
    print(nome, "voto opcional")

else:
    print(nome, "voto obrigatório")
