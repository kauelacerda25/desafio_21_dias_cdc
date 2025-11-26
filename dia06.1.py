#🔹 Exercício 2 — Classificador de Faixa Etária

#Peça ao usuário sua idade e classifique em:

#“Criança” (0–12)

#“Adolescente” (13–17)

#“Adulto” (18–59)

#“Idoso” (60+)

# O programa deve validar a idade (não aceitar valores negativos ou absurdos, como > 130).

idade = int(input("Digite sua idade: "))

if idade < 0 or idade > 130:
    print("Idade inválida!")   
elif idade <= 12:
    print("Criança")    
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")
