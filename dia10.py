# Dia 10: Listas, arrays ou objetos

# Exemplo de lista em Python
frutas = ["maçã", "banana", "laranja", "uva"]
print("Lista de frutas:", frutas)

# Adicionando um item à lista
frutas.append("manga")
print("Após adicionar manga:", frutas)

# Removendo um item da lista
frutas.remove("banana")

print("Após remover banana:", frutas)
# Acessando um item da lista
print("Primeira fruta da lista:", frutas[0])
# Lista de frutas: ['maçã', 'banana', 'laranja', 'uva']
# Após adicionar manga: ['maçã', 'banana', 'laranja', 'uva', 'manga']
# Após remover banana: ['maçã', 'laranja', 'uva', 'manga']
# Primeira fruta da lista: maçã 

# Exemplo de objeto em Python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."   
pessoa1 = Pessoa("Ana", 30)
print(pessoa1.apresentar())
# Olá, meu nome é Ana e tenho 30 anos.
# Atributos do objeto
print("Nome da pessoa:", pessoa1.nome)
print("Idade da pessoa:", pessoa1.idade)
# Nome da pessoa: Ana
# Idade da pessoa: 30
# Modificando atributos do objeto
pessoa1.idade = 31
print("Nova idade da pessoa:", pessoa1.idade)
# Nova idade da pessoa: 31


