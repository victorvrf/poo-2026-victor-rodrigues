# Exercício 2: Unificando Professor e Aluno
# Superclasse Pessoa

class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir_perfil(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")


# Subclasse Professor que herda de Pessoa
class Professor(Pessoa):
    def __init__(self, nome, cpf, email, disciplina):
        super().__init__(nome, cpf, email)
        self.disciplina = disciplina

    def exibir_perfil(self):
        super().exibir_perfil()
        print(f"Disciplina: {self.disciplina}")


# Subclasse Aluno que herda de Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, matricula):
        super().__init__(nome, cpf, email)
        self.matricula = matricula

    def exibir_perfil(self):
        super().exibir_perfil()
        print(f"Matrícula: {self.matricula}")


# Instanciando um professor
professor = Professor(
    "Maria Oliveira",
    "123.456.789-00",
    "maria.oliveira@escola.com",
    "Programação Orientada a Objetos",
)

# Instanciando um aluno
aluno = Aluno(
    "João Silva",
    "987.654.321-00",
    "joao.silva@escola.com",
    "2026001234",
)

# Exibindo os perfis
print("=== Perfil do Professor ===")
professor.exibir_perfil()

print("\n=== Perfil do Aluno ===")
aluno.exibir_perfil()