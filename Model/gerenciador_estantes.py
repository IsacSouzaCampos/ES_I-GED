import pandas as pd
import getpass
import mysql.connector
from mysql.connector import Error

from Model import administrador, login
from View import interface_usuario_estantes
from Model import estante as est
iu_est = interface_usuario_estantes.InterfaceUsuarioEstantes()


class GerenciadorEstantes:
    def __init__(self, estantes):
        self.estantes = estantes

    def adicionar(self, estante):
        try:
            if not self.existe_estante(estante.get_codigo()):
                self.atualizar_sql_adicionar(estante)
                #self.atualizar_csv_adicionar(estante)
                self.estantes.append(estante)
            else:
                # Estante já existente!
                return 1

        except Exception as e:
            raise e

        # Estante adicionada com êxito!
        return 0

    def remover(self, estante, usuario):
        if self.existe_caixa_na_estante(estante):
            # A estante precisa estar vazia para ser removida!
            return 1

        if type(usuario) is not administrador.Administrador:
            nome_admin, senha_admin = iu_est.pedir_dados_administrador()
            admin = login.LogIn().verificar_hierarquia(nome_admin, senha_admin)
            if type(admin) is not administrador.Administrador:
                # Informações de administrador incorretas!
                return 2

        self.atualizar_csv_remover(estante)
        index = self.estantes.index(estante)
        del (self.estantes[index])

        # Estante removida com êxito!
        return 0

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
    def atualizar_sql_adicionar(estante):
        try:
            con = mysql.connector.connect(host='localhost', database='ens', user='root', password='')
            if con.is_connected():
                cursor = con.cursor()
                insert_stmt = (
                    "INSERT INTO estante (codigo_estante, disponibilidade) "
                    "VALUES (%s, %s)"
                )
                data = (estante.get_codigo(), estante.get_disponibilidade())
                cursor.execute(insert_stmt, data)
                con.commit()
                cursor.close()
                con.close()
        except Exception as e:
            raise Exception(f'Erro ao atualizar o banco de dados: {e}')

    @staticmethod
    def atualizar_csv_remover(estante):
        df = pd.read_csv('data/arquivo/estante.csv', encoding='utf-8')
        item = df.loc[df['cod'].astype(str) == str(estante.get_codigo())]
        df = df.drop(item.index)

        df.to_csv('data/arquivo/estante.csv', index=False, encoding='utf-8')

    def get_estante(self, codigo):
        try:
            con = mysql.connector.connect(host='localhost', database='ens', user='root', password='')
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute('SELECT * FROM estante WHERE codigo_estante = %(codigo_est)s', {'codigo_est': int(codigo)})
                linha = cursor.fetchone()
                estante = est.Estante(linha[0], linha[1])
                return estante
        except Exception as e:
            raise Exception(f'Erro ao atualizar o banco de dados: {e}')
