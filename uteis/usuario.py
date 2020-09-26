import getpass


class Usuario:
    def __init__(self, nome=None, codigo_identificacao=None):
        self.nome = nome
        self.numero_identificacao = codigo_identificacao

    @staticmethod
    def adicionar_usuario():
        nome = str(input('Nome do usuario: '))
        senha = getpass.getpass('Senha: ')

        print(nome, senha)

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_codigo_identificacao(self):
        return self.codigo_identificacao

    def set_codigo_identificacao(self, codigo_identificacao):
        self.numero_identificacao = codigo_identificacao
