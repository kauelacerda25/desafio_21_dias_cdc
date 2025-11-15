# Dia 3: Variáveis, tipos e operadores + script simples

# 1. Variáveis

# Uma variável é um nome que armazena um valor na memória.
# Em Python, você não precisa declarar tipo — ele é detectado automaticamente.

# Tipos de variáveis

# String - str (texto)
name = "Kauê"
print(name)    # str

# Inteiro - int (números inteiros)
age = 39
print(age)  # int

# Float - números decimais
temp = 39.5
print(temp) # float

# Bolleanos - verdadeiro ou falto
print(type(True))    # bool


# 2. Opeeradores Aritiméticos

+   # soma
-   # subtração
*   # multiplicação
/   # divisão
//  # divisão inteira
%   # resto
**  # potência

a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000


# Comparação (retornam True/False)

==  # igual
!=  # diferente
>   # maior que
<   # menor que
>=  # maior ou igual
<=  # menor ou igual

# Lógicos

and  # verdadeiro se ambos forem verdade
or   # verdadeiro se ao menos 1 for verdade
not  # inverte o valor


# Script simples: calculadora de IMC

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print(f"\nOlá, {nome}! Seu IMC é {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Peso normal.")
elif imc < 30:
    print("Sobrepeso.")
else:
    print("Obesidade.")
