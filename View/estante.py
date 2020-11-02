import getpass

from Model import estante, administrador, usuario, login


class Estante:
    def adicionar(self, usuario: usuario.Usuario):
        """
        Adiciona uma nova estante ao arquivo
        :param usuario: usuario logado no momento da operação
        """
        est = estante.Estante(str(input('Codigo da estante: ')))
        try:
            if type(usuario) is administrador.Administrador:
                est.adicionar()
                print(f'Estante {est.get_codigo()} adicionada ao arquivo!')
            else:
                nome_admin = str(input('Autorizacao do administrador:\nUsuario: '))
                senha_admin = getpass.getpass('Senha: ').encode()

                admin = login.LogIn().verificar_hierarquia(nome_admin, senha_admin)
                if type(admin) is administrador.Administrador:
                    est.adicionar()
                    print(f'Estante {est.get_codigo()} adicionada ao arquivo!')
                else:
                    raise Exception('Erro na autorização do administrador')

        except Exception as e:
            raise e
