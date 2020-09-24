from src import secao

usuarios = {'Isac': 'senha1', 'Jose': 'senha2'}


class Arquivo:
    secoes = []

    def adicionar_secao(self):
        codigo = str(input('Codigo: '))
        numero_gavetas = int(input('Numero de gavetas: '))
        usuario = str(input('Autorizacao do administrador\nUsuario: '))
        senha = str(input('Senha: '))
        if usuario in usuarios and usuarios[usuario] == senha:
            if self.is_secao_valida(codigo, numero_gavetas):
                nova_secao = secao.Secao()
                nova_secao.set_codigo(codigo)
                nova_secao.set_numero_gavetas(numero_gavetas)
                self.secoes.append(nova_secao)
        else:
            print('Essa conta nao e valida')

    def is_secao_valida(self, codigo, numero_gavetas):
        for _secao in self.secoes:
            if _secao.get_codigo() == codigo:
                print('Codigo de secao ja existente')
                return False
            if numero_gavetas < 1 or numero_gavetas > 20:
                print('Numero de gavetas nao permitido')
                return False
        return True

    def listar_secoes(self):
        for _secao in self.secoes:
            print(_secao.get_codigo())
