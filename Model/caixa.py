import os
import getpass

from Model import administrador, login


class Caixa:
    def __init__(self, estante, codigo):
        self.estante = estante
        self.codigo = codigo

    def adicionar(self, usuario):
        try:
            if self.verificar_existencia():
                raise Exception('Caixa já existente!')

            if type(usuario) is administrador.Administrador:
                os.system(f'touch data/arquivo/{self.get_estante()}/{self.get_codigo()}.csv')
            else:
                nome_admin = str(input('Autorizacao do administrador:\nUsuario: '))
                senha_admin = getpass.getpass('Senha: ').encode()

                admin = login.LogIn().verificar_hierarquia(nome_admin, senha_admin)
                if type(admin) is administrador.Administrador:
                    os.system(f'touch data/arquivo/{self.get_estante()}/{self.get_codigo()}.csv')
                else:
                    raise Exception(f'Erro ao inserir a caixa {self.get_codigo()} no arquivo!')

        except Exception as e:
            raise e

    def verificar_existencia(self) -> bool:
        return os.path.exists(f'data/arquivo/{self.get_estante()}/{self.get_codigo()}.csv')

    def get_estante(self):
        return self.estante

    def set_estante(self, estante):
        self.estante = estante

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
