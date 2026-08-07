# Exercício 1: A Primeira Classe Filha
# Superclasse Veiculo

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


# Subclasse Carro que herda de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas

    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Quantidade de portas: {self.qtd_portas}")


# Instanciando um objeto da classe Carro
carro = Carro("Toyota", "Corolla", 4)

# Exibindo os dados do carro
carro.exibir_dados()