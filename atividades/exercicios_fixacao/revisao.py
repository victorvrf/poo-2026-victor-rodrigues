class Veiculo:
    def __init__(self, marca, modelo, valor_diaria):
        self.marca = marca
        self.modelo = modelo
        self.__valor_diaria = valor_diaria

    def get_valor_diaria(self):
        return self.__valor_diaria

    def calcular_aluguel(self, dias):
        return self.get_valor_diaria() * dias

class Carro(Veiculo):
    def __init__(self, marca, modelo, valor_diaria, portas):
        super().__init__(marca, modelo, valor_diaria)
        self.portas = portas

    def calcular_aluguel(self, dias):
        valor_base = super().calcular_aluguel(dias)
        taxa_limpeza = 50
        return valor_base + taxa_limpeza