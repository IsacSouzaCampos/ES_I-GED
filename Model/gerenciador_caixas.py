import getpass
import pandas as pd

from Model import administrador, login


class GerenciadorCaixas:
    def __init__(self, caixas):
        self.caixas = caixas

    def adicionar(self, caixa, usuario):
        try:
            if self.existe_caixa(caixa.get_codigo()):
                raise Exception('Caixa já existente!')

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
                    raise Exception(f'Erro ao inserir a caixa {caixa.get_codigo()} no arquivo!')

        except Exception as e:
            raise e

    def remover(self, caixa, usuario):
        if caixa.numero_documentos() > 0:
            print(f'numero de documentos = {caixa.numero_documentos()}')
            raise Exception('A caixa precisa estar vazia para ser removida!')
        if type(usuario) is not administrador.Administrador:
            print('Autorização do Administrador:')
            nome_admin = str(input('Usuario: '))
            senha_admin = getpass.getpass('Senha: ').encode()
            if type(login.LogIn().verificar_hierarquia(nome_admin, senha_admin)) is not administrador.Administrador:
                raise Exception('Informações de administrador incorretas!')
        self.atualizar_csv_remover(caixa)
        index = self.caixas.index(caixa)
        print(f'index = {index}')
        del (self.caixas[index])
        print('Caixa removida com êxito!')

    def remover_documento_de_caixa(self, documento):
        temp = None
        for caixa in self.caixas:
            for _documento in caixa.documentos:
                if documento == _documento:
                    index = self.caixas.index(caixa)
                    temp = caixa
                    del(self.caixas[index])

        docs = temp.get_documentos()
        index = docs.index(documento)
        del(docs[index])
        temp.set_documentos(docs)

        self.caixas.append(temp)

    @staticmethod
    def atualizar_csv_adicionar(caixa):
        try:
            df = pd.DataFrame({'cod': [caixa.get_codigo()],
                               'cod_est': [caixa.get_estante().get_codigo()]})

            with open(f'data/arquivo/caixa.csv', encoding='utf-8') as fin:
                if not fin.read():
                    df.to_csv(f'data/arquivo/caixa.csv', index=False, encoding='utf-8')
                else:
                    df_caixa = pd.read_csv(f'data/arquivo/caixa.csv', encoding='utf-8')
                    pd.concat([df, df_caixa]).to_csv(f'data/arquivo/caixa.csv', index=False, encoding='utf-8')

        except Exception as e:
            raise Exception(f'Erro ao atualizar o banco de dados: {e}')

    @staticmethod
    def atualizar_csv_remover(caixa):
        df = pd.read_csv('data/arquivo/caixa.csv', encoding='utf-8')
        item = df.loc[df['cod'].astype(str) == str(caixa.get_codigo())]
        df = df.drop(item.index)
        print(df)

        df.to_csv('data/arquivo/caixa.csv', index=False, encoding='utf-8')

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
