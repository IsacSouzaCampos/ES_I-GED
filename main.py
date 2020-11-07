from View import login, caixa, documento, estante


def main():
    try:
        usuario = login.LogIn().login()
    except Exception as e:
        print(e)
        return

    opcao = -1
    while opcao != 0:
        opcao = mostrar_interface()
        try:
            if opcao == 1:
                documento.Documento().adicionar()
            elif opcao == 2:
                caixa.Caixa().adicionar(usuario)
            elif opcao == 3:
                documento.Documento().anexar(usuario)
            elif opcao == 4:
                estante.Estante().adicionar(usuario)
            elif opcao == 5:
                documento.Documento().listar()
            elif opcao == 6:
                documento.Documento().pesquisar()
            elif opcao == 7:
                documento.Documento().tramitar(usuario)
        except Exception as e:
            print(e)


def mostrar_interface() -> int:
    print('=' * 20)
    print('[1] Adicionar documento')
    print('[2] Adicionar caixa ao arquivo')
    print('[3] Anexar documentos')
    print('[4] Adicionar estante ao arquivo')
    print('[5] Listar documentos de uma caixa')
    print('[6] Pesquisar documento')
    print('[7] Tramitar')
    print('[0] Sair')
    return int(input('Opcao: '))


if __name__ == '__main__':
    main()
