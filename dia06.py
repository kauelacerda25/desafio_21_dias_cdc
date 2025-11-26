#🔹 Exercício 1 — Sistema de Pontuação de Jogo

#Crie um programa que receba três valores:

#Pontos iniciais

#Pontos ganhos

#Pontos perdidos

#O programa deve calcular e exibir a pontuação final do jogador.
# #Regras adicionais:
#Se a pontuação final for negativa, exibir uma mensagem especial dizendo que o jogador “zerou as energias”.
#Se a pontuação final for maior que 100, exibir “nível avançado”.

p1 = int(input("Pontos iniciais: "))
p2 = int(input("Pontos ganhos: "))
p3 = int(input("Pontos perdidos: "))

pontuacao_final = p1 + p2 - p3

print("Pontuação final:", pontuacao_final)
if pontuacao_final < 0:
    print("Jogador zerou as energias!")
elif pontuacao_final > 100:
    print("Nível avançado!")
