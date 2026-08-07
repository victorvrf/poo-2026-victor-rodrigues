# Exercício 3: Sistema de Cadastro de Produtos
# Classe mãe Produto

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        self.preco = self.preco * (1 - porcentagem / 100)


# Subclasse Livro que herda de Produto
class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor


# Subclasse Eletronico que herda de Produto
class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


# Instanciando um livro e um eletrônico
livro = Livro("Dom Casmurro", 50.00, "Machado de Assis")
eletronico = Eletronico("Smartphone", 2000.00, 110)

# Aplicando os descontos
livro.aplicar_desconto(15)
eletronico.aplicar_desconto(10)

# Exibindo os novos preços
print(f"Livro: {livro.nome} (autor: {livro.autor})")
print(f"Novo preço do livro: R$ {livro.preco:.2f}")

print(f"\nEletrônico: {eletronico.nome} (voltagem: {eletronico.voltagem}V)")
print(f"Novo preço do eletrônico: R$ {eletronico.preco:.2f}")