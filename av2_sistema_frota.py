# AV2 - Sistema de Gestão de Frota e Locação de Veículos
# Trabalho prático de POO: herança, encapsulamento, polimorfismo e tratamento de exceções.


class Veiculo:
    """Superclasse que representa um veículo genérico da frota."""

    def __init__(self, modelo, placa, valor_diaria):
        # Atributos privados (encapsulamento).
        # Os valores iniciais são neutros; a validação acontece nos setters.
        self.__modelo = ""
        self.__placa = ""
        self.__valor_diaria = 0.0
        self.set_modelo(modelo)
        self.set_placa(placa)
        self.set_valor_diaria(valor_diaria)

    # ------------------------- Getters -------------------------
    def get_modelo(self):
        return self.__modelo

    def get_placa(self):
        return self.__placa

    def get_valor_diaria(self):
        return self.__valor_diaria

    def get_tipo(self):
        return "Veículo"

    # ------------------ Setters com validação ------------------
    def set_modelo(self, valor):
        valor = str(valor).strip()
        if not valor:
            raise ValueError("O modelo não pode ficar em branco.")
        self.__modelo = valor

    def set_placa(self, valor):
        valor = str(valor).strip().upper()
        if not valor:
            raise ValueError("A placa não pode ficar em branco.")
        self.__placa = valor

    def set_valor_diaria(self, valor):
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError("O valor da diária deve ser um número.")
        if valor <= 0:
            raise ValueError("O valor da diária deve ser maior que zero.")
        self.__valor_diaria = valor

    # ------------------- Regra de negócio ----------------------
    def calcular_aluguel(self, dias):
        """Valor base do aluguel: diária x quantidade de dias.

        As subclasses sobrescrevem este método aplicando regras próprias.
        """
        if dias <= 0:
            raise ValueError("A quantidade de dias deve ser maior que zero.")
        return dias * self.get_valor_diaria()

    def exibir_dados(self):
        print(f"  Tipo........: {self.get_tipo()}")
        print(f"  Modelo......: {self.get_modelo()}")
        print(f"  Placa.......: {self.get_placa()}")
        print(f"  Diária......: R$ {self.get_valor_diaria():.2f}")


class Carro(Veiculo):
    """Subclasse que representa um carro, com a quantidade de portas."""

    TAXA_LIMPEZA = 50.00

    def __init__(self, modelo, placa, valor_diaria, portas):
        super().__init__(modelo, placa, valor_diaria)
        self.__portas = 0
        self.set_portas(portas)

    def get_portas(self):
        return self.__portas

    def get_tipo(self):
        return "Carro"

    def set_portas(self, valor):
        try:
            valor = int(valor)
        except ValueError:
            raise ValueError("A quantidade de portas deve ser um número inteiro.")
        if valor <= 0:
            raise ValueError("A quantidade de portas deve ser maior que zero.")
        self.__portas = valor

    def calcular_aluguel(self, dias):
        # Sobrescrita: valor base do aluguel + taxa de limpeza de R$ 50,00.
        return super().calcular_aluguel(dias) + Carro.TAXA_LIMPEZA

    def exibir_dados(self):
        super().exibir_dados()
        print(f"  Portas......: {self.get_portas()}")


class Moto(Veiculo):
    """Subclasse que representa uma moto, com as cilindradas."""

    DESCONTO = 0.10

    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)
        self.__cilindradas = 0
        self.set_cilindradas(cilindradas)

    def get_cilindradas(self):
        return self.__cilindradas

    def get_tipo(self):
        return "Moto"

    def set_cilindradas(self, valor):
        try:
            valor = int(valor)
        except ValueError:
            raise ValueError("As cilindradas devem ser um número inteiro.")
        if valor <= 0:
            raise ValueError("As cilindradas devem ser maiores que zero.")
        self.__cilindradas = valor

    def calcular_aluguel(self, dias):
        # Sobrescrita: valor base do aluguel com 10% de desconto.
        return super().calcular_aluguel(dias) * (1 - Moto.DESCONTO)

    def exibir_dados(self):
        super().exibir_dados()
        print(f"  Cilindradas.: {self.get_cilindradas()}")


# Lista centralizada que armazena objetos heterogêneos (Carro e Moto).
frota = []


def cadastrar_carro():
    """Solicita os dados e cadastra um Carro na frota."""
    print("\n--- Cadastro de Carro ---")
    try:
        # Os dados são lidos como texto e enviados ao construtor.
        # A conversão e a validação acontecem nos setters da classe.
        modelo = input("Modelo..........: ")
        placa = input("Placa...........: ")
        valor_diaria = input("Valor da diária: R$ ")
        portas = input("Portas..........: ")
        veiculo = Carro(modelo, placa, valor_diaria, portas)
    except ValueError as erro:
        print(f">> Não foi possível cadastrar: {erro}")
    else:
        frota.append(veiculo)
        print(f">> Carro de placa '{veiculo.get_placa()}' cadastrado com sucesso!")
    finally:
        print("--- Fim do cadastro de carro ---")


def cadastrar_moto():
    """Solicita os dados e cadastra uma Moto na frota."""
    print("\n--- Cadastro de Moto ---")
    try:
        # Os dados são lidos como texto e enviados ao construtor.
        # A conversão e a validação acontecem nos setters da classe.
        modelo = input("Modelo..........: ")
        placa = input("Placa...........: ")
        valor_diaria = input("Valor da diária: R$ ")
        cilindradas = input("Cilindradas.....: ")
        veiculo = Moto(modelo, placa, valor_diaria, cilindradas)
    except ValueError as erro:
        print(f">> Não foi possível cadastrar: {erro}")
    else:
        frota.append(veiculo)
        print(f">> Moto de placa '{veiculo.get_placa()}' cadastrada com sucesso!")
    finally:
        print("--- Fim do cadastro de moto ---")


def listar_frota():
    """Exibe todos os veículos cadastrados."""
    print("\n--- Frota cadastrada ---")
    if not frota:
        print(">> Nenhum veículo cadastrado até o momento.")
        return
    indice = 1
    for veiculo in frota:
        print(f"\n[{indice}]")
        veiculo.exibir_dados()
        indice = indice + 1


def calcular_alugueis_todos():
    """Calcula o aluguel de toda a frota usando polimorfismo."""
    print("\n--- Aluguel de todos os veículos ---")
    if not frota:
        print(">> Nenhum veículo cadastrado até o momento.")
        return

    try:
        dias = int(input("Quantidade de dias de aluguel: "))
    except ValueError:
        print(">> Entrada inválida! Digite um número inteiro de dias.")
        return

    if dias <= 0:
        print(">> A quantidade de dias deve ser maior que zero.")
        return

    total = 0.0
    try:
        # Laço polimórfico: cada objeto responde com a sua própria regra.
        for veiculo in frota:
            valor = veiculo.calcular_aluguel(dias)
            total = total + valor
            print(f"  {veiculo.get_tipo():<6} {veiculo.get_placa():<10} -> R$ {valor:.2f}")
    except ValueError as erro:
        print(f">> Erro ao calcular o aluguel: {erro}")
    else:
        print(f"\n  Total da frota por {dias} dia(s): R$ {total:.2f}")
    finally:
        print("--- Fim do cálculo de aluguel ---")


def buscar_por_placa():
    """Busca um veículo pela placa informada, tratando o erro de busca."""
    print("\n--- Buscar veículo por placa ---")
    if not frota:
        print(">> Nenhum veículo cadastrado até o momento.")
        return

    placa = input("Informe a placa desejada: ").strip().upper()

    encontrado = None
    for veiculo in frota:
        if veiculo.get_placa() == placa:
            encontrado = veiculo
            break

    try:
        if encontrado is None:
            raise ValueError(f"Nenhum veículo com a placa '{placa}' foi encontrado.")
    except ValueError as erro:
        print(f">> {erro}")
    else:
        print(">> Veículo encontrado:")
        encontrado.exibir_dados()
    finally:
        print("--- Fim da busca ---")


def exibir_menu():
    """Mostra as opções do menu principal."""
    print("\n" + "=" * 46)
    print("   SISTEMA DE GESTÃO DE FROTA E LOCAÇÃO")
    print("=" * 46)
    print("1 - Cadastrar Carro")
    print("2 - Cadastrar Moto")
    print("3 - Listar frota")
    print("4 - Calcular aluguel de todos os veículos")
    print("5 - Buscar veículo por placa")
    print("6 - Sair")
    print("=" * 46)


def main():
    """Menu interativo principal. Nunca encerra por causa de entrada inválida."""
    print("Bem-vindo(a) ao Sistema de Gestão de Frota e Locação de Veículos!")

    while True:
        try:
            exibir_menu()
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                cadastrar_carro()
            elif opcao == 2:
                cadastrar_moto()
            elif opcao == 3:
                listar_frota()
            elif opcao == 4:
                calcular_alugueis_todos()
            elif opcao == 5:
                buscar_por_placa()
            elif opcao == 6:
                print("\n>> Encerrando o sistema. Até logo!")
                break
            else:
                print(">> Opção inexistente! Escolha um número de 1 a 6.")
        except ValueError:
            print(">> Entrada inválida! Digite um número inteiro para a opção do menu.")
        except (KeyboardInterrupt, EOFError):
            print("\n>> Entrada interrompida pelo usuário. Encerrando o sistema...")
            break


if __name__ == "__main__":
    main()
