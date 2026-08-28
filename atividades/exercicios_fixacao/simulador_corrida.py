"""
Atividade Prática: Simulação de Corrida com Polimorfismo
Disciplina: Programação e Desenvolvimento de Software
Conteúdo: Polimorfismo e Interfaces em Python

Simulador de Corrida de Veículos em Python, onde múltiplos objetos
de tipos diferentes (Carro, Moto, Caminhão) são executados em conjunto
através de uma única interface comum.
"""

from abc import ABC, abstractmethod


class Veiculo(ABC):
    """
    Classe abstrata (interface) que define o contrato comum
    para todos os veículos da corrida.
    """

    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        """Método abstrato que cada veículo deve sobrescrever."""
        pass


class Carro(Veiculo):
    """Classe filha que herda de Veiculo e sobrescreve acelerar()."""

    def acelerar(self):
        print(f"O carro {self.modelo} acelerou com o motor potente! Vrum vrum!!")


class Moto(Veiculo):
    """Classe filha que herda de Veiculo e sobrescreve acelerar()."""

    def acelerar(self):
        print(f"A moto {self.modelo} acelerou com uma arrancada esportiva! Rammm!!")


class Caminhao(Veiculo):
    """Classe filha que herda de Veiculo e sobrescreve acelerar()."""

    def acelerar(self):
        print(f"O caminhão {self.modelo} acelerou pesadamente, carregando muita carga!")


class CarroEletrico(Veiculo):
    """Classe extra (bônus) que herda de Veiculo e sobrescreve acelerar()."""

    def acelerar(self):
        print(f"O carro elétrico {self.modelo} acelerou instantaneamente em silêncio!")


def executar_corrida():
    """Executa a simulação de corrida usando a execução polimórfica."""

    # Lista heterogênea: objetos de tipos diferentes tratados como Veiculo
    pista_de_corrida = [
        Carro("Ferrari F8 Tributo"),
        Moto("Honda CBR 1000RR"),
        Caminhao("Mercedes-Benz Actros"),
        CarroEletrico("Tesla Model S"),  # Desafio bônus: novo veículo na lista
    ]

    print("=" * 60)
    print(" SIMULAÇÃO DE CORRIDA - POLIMORFISMO EM AÇÃO ".center(60, "="))
    print("=" * 60)

    # Execução polimórfica: uma única chamada para tipos diferentes
    for veiculo in pista_de_corrida:
        veiculo.acelerar()

    print("=" * 60)
    print(" FIM DA CORRIDA ".center(60, "="))
    print("=" * 60)


if __name__ == "__main__":
    executar_corrida()