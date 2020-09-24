from src import arquivo, secao, documento, processo, usuario, usuarioComum, administrador


def main():
    administrador1 = administrador.Administrador('Isac', 0)
    print('Nome:', administrador1.get_nome())
    print('Numero:', administrador1.get_numero_identificacao())
    # arquivo_ = arquivo.Arquivo()
    # arquivo_.adicionar_secao()
    #
    # arquivo_.listar_secoes()


if __name__ == '__main__':
    main()
