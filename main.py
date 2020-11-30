from View import login, gerenciador_caixas as gcv, gerenciador_documentos as gdv, gerenciador_estantes as gev
from Model import arquivo as arq, administrador


usuario = administrador.Administrador()
ger_est, ger_cx, ger_doc = arq.Arquivo().carregar_arquivo()


def main():
    opcao = -1
    while opcao != 0:
        opcao = mostrar_interface()
        try:
            if opcao == 1:
                adicionar_estante()
            elif opcao == 2:
                adicionar_caixa()
            elif opcao == 3:
                adicionar_documento()
            elif opcao == 4:
                anexar_documentos()
            elif opcao == 5:
                listar_documentos_caixa()
            elif opcao == 6:
                pesquisar_documento()
            elif opcao == 7:
                tramitar()
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


def adicionar_estante():
    codigo, disponibilidade = gev.GerenciadorEstantes().adicionar(usuario)
    ger_est.adicionar(codigo, disponibilidade)


def adicionar_caixa():
    codigo, codigo_estante = gcv.GerendiadorCaixas().adicionar()
    if ger_est.existe_estante(codigo_estante):
        if ger_est.possui_disponibilidade(codigo_estante):
            ger_cx.adicionar(codigo, codigo_estante, usuario)
            ger_est.atualizar_csv_disponibilidade(codigo_estante)
        else:
            print('Estante indisponivel no momento!')
    else:
        print('Estante nao encontrada!')


def adicionar_documento():
    documento = gdv.GerenciadorDocumentos().adicionar()
    codigo_caixa = documento.get_codigo_caixa()
    caixa = ger_cx.get_caixa(codigo_caixa)
    ger_doc.adicionar(documento, caixa.get_codigo_estante())


def anexar_documentos():
    # protocolo1, protocolo2 = gdv.GerenciadorDocumentos().anexar()
    protocolo1 = '0'
    protocolo2 = '1'
    documento1 = ger_doc.pesquisar('protocolo', protocolo1)[0]
    documento2 = ger_doc.pesquisar('protocolo', protocolo2)[0]
    caixa_d2 = ger_cx.get_caixa(documento2.get_codigo_caixa())
    codigo_estante_d2 = caixa_d2.get_codigo_estante()
    ger_doc.anexar(documento1, documento2, codigo_estante_d2, usuario.get_nome())


def listar_documentos_caixa():
    codigo_caixa = gdv.GerenciadorDocumentos().listar_documentos_caixa()
    documentos = ger_doc.listar_documentos_caixa(codigo_caixa)
    for documento in documentos:
        caixa = ger_cx.get_caixa(documento.get_codigo_caixa())
        codigo_estante = caixa.get_codigo_estante()
        documento.imprimir(codigo_estante)


def pesquisar_documento():
    forma_pesquisa, dado_pesquisado = gdv.GerenciadorDocumentos().pesquisar()
    documentos = ger_doc.pesquisar(forma_pesquisa, dado_pesquisado)
    for documento in documentos:
        codigo_estante = ger_cx.get_caixa(documento.get_codigo_caixa()).get_codigo_estante()
        documento.imprimir(codigo_estante)


def tramitar():
    protocolo, codigo_caixa, motivo = gdv.GerenciadorDocumentos().tramitar()
    caixa = ger_cx.get_caixa(codigo_caixa)
    codigo_estante = caixa.get_codigo_estante()
    ger_doc.tramitar(protocolo, codigo_caixa, codigo_estante, motivo, usuario.get_nome())


if __name__ == '__main__':
    main()
