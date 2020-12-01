import getpass
import pandas as pd

from Model import administrador, login, caixa as cx


class GerenciadorCaixas:
    def __init__(self, caixas):
        self.caixas = caixas

    def adicionar(self, codigo, codigo_estante, usuario):
        try:
            if self.existe_caixa(codigo):
                raise Exception('Caixa já existente!')

            caixa = cx.Caixa(codigo, codigo_estante)

            if type(usuario) is administrador.Administrador:
                self.atualizar_csv_adicionar(caixa)
                self.caixas.append(caixa)
            else:
                nome_admin = str(input('Autorizacao do administrador:\nUsuario: '))
                senha_admin = getpass.getpass('Senha: ').encode()

                admin = login.LogIn().verificar_hierarquia(nome_admin, senha_admin)
                if type(admin) is administrador.Administrador:
                    self.atualizar_csv_adicionar(caixa)
                    self.caixas.append(caixa)
                else:
                    raise Exception(f'Erro ao inserir a caixa {codigo} no arquivo!')

        except Exception as e:
            raise e

    @staticmethod
    def atualizar_csv_adicionar(caixa):
        try:
            df = pd.DataFrame({'cod': [caixa.get_codigo()],
                               'cod_est': [caixa.get_codigo_estante()]})

            with open(f'data/arquivo/caixa.csv', encoding='utf-8') as fin:
                if not fin.read():
                    df.to_csv(f'data/arquivo/caixa.csv', index=False, encoding='utf-8')
                else:
                    df_caixa = pd.read_csv(f'data/arquivo/caixa.csv', encoding='utf-8')
                    pd.concat([df, df_caixa]).to_csv(f'data/arquivo/caixa.csv', index=False, encoding='utf-8')

        except Exception as e:
            raise Exception(f'Erro ao atualizar o banco de dados: {e}')

    def existe_caixa(self, codigo):
        try:
            self.get_caixa(codigo)
            return True
        except:
            return False

    def get_caixa(self, codigo):
        for caixa in self.caixas:
            if str(codigo) == str(caixa.get_codigo()):
                return caixa
        raise Exception('Caixa não encontrada!')
