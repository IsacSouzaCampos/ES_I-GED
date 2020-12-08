import pandas as pd
import getpass

from Model import administrador, login


class GerenciadorEstantes:
    def __init__(self, estantes):
        self.estantes = estantes

    def adicionar(self, estante):
        try:
            if not self.existe_estante(estante.get_codigo()):
                self.atualizar_csv_adicionar(estante)
                self.estantes.append(estante)
            else:
                raise Exception('Estante ja existente!')
        except Exception as e:
            raise e

    def remover(self, estante, usuario):
        if self.existe_caixa_na_estante(estante):
            raise Exception('A estante precisa estar vazia para ser removida!')
        if type(usuario) is not administrador.Administrador:
            print('Autorização do Administrador:')
            nome_admin = str(input('Usuario: '))
            senha_admin = getpass.getpass('Senha: ').encode()
            if type(login.LogIn().verificar_hierarquia(nome_admin, senha_admin)) is not administrador.Administrador:
                raise Exception('Informações de administrador incorretas!')
        self.atualizar_csv_remover(estante)
        index = self.estantes.index(estante)
        del (self.estantes[index])
        print('Estante removida com êxito!')

    @staticmethod
    def existe_caixa_na_estante(estante):
        df = pd.read_csv('data/arquivo/caixa.csv', encoding='utf-8')
        for index, row in df.iterrows():
            if str(row['cod_est']) == str(estante.get_codigo()):
                return True
        return False

    def existe_estante(self, codigo):
        try:
            self.get_estante(codigo)
            return True
        except:
            return False

    def possui_disponibilidade(self, codigo):
        if int(self.get_estante(codigo).get_disponibilidade()) > 0:
            return True
        return False

    def atualizar_csv_disponibilidade(self, codigo, disponibilidade):
        for estante in self.estantes:
            if str(estante.get_codigo()) == str(codigo):
                estante.set_disponibilidade(disponibilidade)

        df = pd.read_csv('data/arquivo/estante.csv', encoding='utf-8')
        df.loc[df['cod'].astype(str) == str(codigo), ['disponibilidade']] = disponibilidade
        df.to_csv('data/arquivo/estante.csv', index=False, encoding='utf-8')

    @staticmethod
    def atualizar_csv_adicionar(estante):
        try:
            df = pd.DataFrame({'cod': [estante.get_codigo()],
                               'disponibilidade': [estante.get_disponibilidade()]})

            with open(f'data/arquivo/estante.csv', encoding='utf-8') as fin:
                if not fin.read():
                    df.to_csv(f'data/arquivo/estante.csv', index=False, encoding='utf-8')
                else:
                    df_caixa = pd.read_csv(f'data/arquivo/estante.csv', encoding='utf-8')
                    pd.concat([df, df_caixa]).to_csv(f'data/arquivo/estante.csv', index=False, encoding='utf-8')

        except Exception as e:
            raise Exception(f'Erro ao atualizar o banco de dados: {e}')

    @staticmethod
    def atualizar_csv_remover(estante):
        df = pd.read_csv('data/arquivo/estante.csv', encoding='utf-8')
        item = df.loc[df['cod'].astype(str) == str(estante.get_codigo())]
        df = df.drop(item.index)

        df.to_csv('data/arquivo/estante.csv', index=False, encoding='utf-8')

    def get_estante(self, codigo):
        for estante in self.estantes:
            if str(codigo) == str(estante.get_codigo()):
                return estante
        raise Exception('Estante não encontrada!')
