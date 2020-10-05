import getpass

class usuario:
    def __init__(self, nome=None, codigo_identificacao=None):
        self.nome = nome
        self.numero_identificacao = codigo_identificacao

    @staticmethod
    def adicionar_usuario():
        nome = str(input('Nome do usuario: '))
        senha = getpass.getpass('Senha: ')

        print(nome, senha)