# Dia 4: Estruturas condicionais (if/else)
# Em Python, usamos if, elif e else para tomar decisões no código, executando partes diferentes dependendo das condições.

idade = 20

if idade >= 18:
    print("Você é maior de idade.")  # bloco de código executado se a condição for verdadeira

# Usamos else quando queremos executar algo caso o if seja falso.


idade = 15

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")  # bloco de código executado se a condição for falsa


# O elif permite testar múltiplas condições.

nota = 7

if nota >= 9:
    print("Aprovado com excelência")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
# Podemos aninhar estruturas condicionais para criar decisões mais complexas.