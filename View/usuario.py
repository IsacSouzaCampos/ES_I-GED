import getpass

class usuario:
    def __init__(self, nome=None):
        self.nome = nome

    @staticmethod
    def adicionar_usuario():
        nome = str(input('Nome do usuario: '))
        senha = getpass.getpass('Senha: ')

        print(nome, senha)