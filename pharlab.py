from pathlib import Path
import shutil


raiz = Path('.')
arquivos_raiz = raiz.iterdir()
arquivos_raiz_pedidos = list()
pastas = 'Pedidos'
pedidos = list()
diretorio = Path('pedidos')
arquivos = diretorio.iterdir()

if diretorio.exists():
    pass
else:
    Path('pedidos').mkdir()


for x in arquivos:
    pedidos.append(x)

for x in arquivos_raiz:
    if x.is_file():
        nome_arquivo = x.name
        if nome_arquivo.startswith('PHL'):
            shutil.move(nome_arquivo, diretorio)


def pharlab_pedido(file: str) -> str:
    produtos = list()
    qtde_produtos = list()
    with open(file=file, mode='r', encoding='utf8', errors='ignore') as arquivo:
        linha = arquivo.readline()

        while linha:

            if linha.startswith('01'):
                layout = linha[2:5]
                cnpj = linha[5:19]

            if linha.startswith('02'):
                pedido = linha[5:15]

            if linha.startswith('03'):
                tipoPagamento = linha[2:4]
            
            if linha.startswith('04'):
                pass

            if linha.startswith('05'):
                ean = linha[2:15]
                qtde = int(linha[42:53])
                produtos.append(ean)
                qtde_produtos.append(qtde)

                   

            linha = arquivo.readline()
        print('-' * 77)
        print(f'Pedido: {pedido} Arquivo:  {file.name}|')
        print('-' * 77)
        print(f'CNPJ: {cnpj}')
        print(f'Layout: {layout}')
        print(f'Tipo Pagamento {tipoPagamento}')
        for produto, qtde in zip(produtos, qtde_produtos):
            print(f'EAN {produto} - Quantidade: {qtde}')


if diretorio.iterdir():
    #print(f'PEDIDO;CNPJ;ARQUIVO;EMAIL')
    for arquivo in pedidos:
        pharlab_pedido(arquivo)
else:
    None
