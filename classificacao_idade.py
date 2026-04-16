idade = int(input("Digite sua idade: "))

if idade <= 12:
    print (idade ,"é criança")
elif idade >= 13 and idade <= 17:
    print (idade ,"é adolescente")  
else:
    print (idade ,"é adulto")