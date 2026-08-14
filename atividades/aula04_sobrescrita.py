class Funcionario:
    def __init__(self, nome: str, salario_base: float):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_bonus(self) -> float:
        return self.salario_base * 0.05


class Gerente(Funcionario):
    def calcular_bonus(self) -> float:  
        bonus_padrao = super().calcular_bonus()
        return bonus_padrao + 1000.00


class Vendedor(Funcionario):
    def __init__(self, nome: str, salario_base: float, total_vendas: float):
        super().__init__(nome, salario_base)
        self.total_vendas = total_vendas

    def calcular_bonus(self) -> float:
        
        return self.total_vendas * 0.10


def executar_testes():
    """Script de teste para validar o comportamento das classes."""
    print("=" * 50)
    print(" INICIANDO TESTE DO SISTEMA DE BÔNUS ".center(50, "="))
    print("=" * 50)


    f = Funcionario("Carlos Silva", 3000.00)
    bonus_f = f.calcular_bonus()
    print(f"Funcionario: {f.nome}")
    print(f"   Salario Base: R$ {f.salario_base:.2f}")
    print(f"   Bonus Calculado: R$ {bonus_f:.2f} (Esperado: R$ 150.00)")
    print("-" * 50)

  
    g = Gerente("Ana Souza", 5000.00)
    bonus_g = g.calcular_bonus()
    print(f"Gerente: {g.nome}")
    print(f"   Salario Base: R$ {g.salario_base:.2f}")
    print(f"   Bonus Calculado: R$ {bonus_g:.2f} (Esperado: R$ 1250.00)")
    print("-" * 50)

   
    bonus_v = v.calcular_bonus()
    print(f"Vendedor: {v.nome}")
    print(f"   Salario Base: R$ {v.salario_base:.2f}")
    print(f"   Total de Vendas: R$ {v.total_vendas:.2f}")
    print(f"   Bonus Calculado: R$ {bonus_v:.2f} (Esperado: R$ 1500.00)")
    print("=" * 50)
    print(" FIM DO TESTE ".center(50, "="))
    print("=" * 50)



if __name__ == "__main__":
    executar_testes()
