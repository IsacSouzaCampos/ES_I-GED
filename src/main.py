from src import arquivo, secao, documento, processo, usuario, usuarioComum


def main():
    arquivo_ = arquivo.Arquivo()
    arquivo_.adicionar_secao()

    arquivo_.listar_secoes()


if __name__ == '__main__':
    main()
