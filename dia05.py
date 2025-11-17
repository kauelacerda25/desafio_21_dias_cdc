#Dia 5: Laços de repetição (for/while)

# 1. for — Quando você sabe quantas vezes quer repetir
# O for percorre itens de uma sequência (lista, string, range, etc.)

for i in range(5):
    print(i)

#2. while — Quando você repete até uma condição ser falsa

x = 0

while x < 5:
    print(x)
    x += 1

#3.  break — Interrompe o laço

for i in range(10):
    if i == 5:
        break
    print(i)

#4. continue — Pula para a próxima iteração do laço

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#5. else — Executa um bloco quando o laço termina normalmente

for i in range(5):
    print(i)
else:
    print("Laço concluído")

# Exemplo prático: menu repetitivo

while True:
    print("1 - Olá")
    print("2 - Sair")

    op = input("Escolha: ")

    if op == "1":
        print("Olá!")
    elif op == "2":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
