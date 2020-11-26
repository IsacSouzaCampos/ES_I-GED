import getpass

from Model import estante, administrador, usuario, login


class GerenciadorEstantes:
    def adicionar(self, usuario: usuario.Usuario):
        codigo = str(input('Codigo da estante: '))
        disponibilidade = str(input('Disponibilidade da estante: '))
        try:
            if type(usuario) is administrador.Administrador:
                return codigo, disponibilidade
            else:
                nome_admin = str(input('Autorizacao do administrador:\nUsuario: '))
                senha_admin = getpass.getpass('Senha: ').encode()

                admin = login.LogIn().verificar_hierarquia(nome_admin, senha_admin)
                if type(admin) is administrador.Administrador:
                    return codigo, disponibilidade
                else:
                    raise Exception('Erro na autorização do administrador')

        except Exception as e:
            raise e
