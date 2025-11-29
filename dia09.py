# Dia 9: Funções e modularização

def saudacao(nome):
    """Retorna uma saudação personalizada."""
    print(f"Olá, {nome}! Bem-vindo ao módulo de funções.")

saudacao("Kauê")

#  Olá, {nome}! Bem-vindo ao módulo de funções." 
#  Exemplo de função simples que imprime uma saudação personalizada.   
def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b 
resultado = soma(5, 3)
print(f"A soma de 5 e 3 é: {resultado}")
# A soma de 5 e 3 é: 8

# Exemplo de função que retorna a soma de dois números.
def fatorial(n):
    """Retorna o fatorial de um número."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
resultado = fatorial(5)
print(f"O fatorial de 5 é: {resultado}")
# O fatorial de 5 é: 120

