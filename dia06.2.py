#🔹 Exercício 3 — Controle de Estoque

#Crie um programa que:

#Pergunte a quantidade atual de um produto no estoque.

#Pergunte o limite mínimo.

#Pergunte a quantidade que será adicionada ou removida (valor pode ser negativo).

#Após atualizar o estoque, o programa deve:

#Exibir a nova quantidade.

#Informar se está abaixo do limite, no limite, ou acima do limite.

#Solicitar a quantidade atual de um produto no estoque
quantidade_estoque = int(input("Digite a quantidade atual do produto no estoque: "))
#Solicitar o limite mínimo do produto
limite_minimo = int(input("Digite o limite mínimo do produto: "))
#Solicitar a quantidade que será adicionada ou removida
quantidade_alteracao = int(input("Digite a quantidade a ser adicionada (positivo) ou removida (negativo): "))
#Atualizar a quantidade no estoque 
quantidade_estoque += quantidade_alteracao
#Exibir a nova quantidade no estoque
print(f"A nova quantidade no estoque é: {quantidade_estoque}")
#Verificar se o estoque está abaixo, no limite ou acima do limite  
if quantidade_estoque < limite_minimo:
    print("O estoque está abaixo do limite mínimo.")
elif quantidade_estoque == limite_minimo:
    print("O estoque está no limite mínimo.")
else:
    print("O estoque está acima do limite mínimo.")
