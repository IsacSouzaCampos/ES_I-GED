from View import login, gerenciador_caixas as gcv, gerenciador_documentos as gdv, gerenciador_estantes as gev
from Model import arquivo as arq
from Model import estante as estm, caixa as cxm, documento as docm


def main():
    try:
        usuario = login.LogIn().login()
        ger_est, ger_cx, ger_doc = arq.Arquivo().carregar_arquivo()
    except Exception as e:
        print(e)
        return

    opcao = -1
    while opcao != 0:
        opcao = mostrar_interface()
        try:
            if opcao == 1:
                codigo = gev.GerenciadorEstantes().adicionar(usuario)
                ger_est.adicionar(codigo)
            elif opcao == 2:
                codigo, codigo_estante = gcv.GerendiadorCaixas().adicionar()
                if ger_est.existe_estante(codigo_estante):
                    ger_cx.adicionar(codigo, codigo_estante, usuario)
            elif opcao == 3:
                documento = gdv.GerenciadorDocumentos().adicionar()
                codigo_caixa = documento.get_codigo_caixa()
                caixa = ger_cx.get_caixa(codigo_caixa)
                ger_doc.adicionar(documento, caixa.get_codigo_estante())
            elif opcao == 4:
                pass
            elif opcao == 5:
                pass
            elif opcao == 6:
                pass
            elif opcao == 7:
                pass
        except Exception as e:
            print(e)


def mostrar_interface() -> int:
    print('=' * 20)
    print('[1] Adicionar estante')
    print('[2] Adicionar caixa')
    print('[3] Adicionar documento')
    print('[4] Anexar documentos')
    print('[5] Listar documentos de uma caixa')
    print('[6] Pesquisar documento')
    print('[7] Tramitar')
    print('[0] Sair')
    return int(input('Opcao: '))


if __name__ == '__main__':
    main()
