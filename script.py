import os
import base64

# Caminho da pasta com os XMLs
PASTA_XML = './data'
LOTE_TAMANHO = 3
PASTA_SAIDA = './out'


def listar_arquivos_xml(pasta):
    return [f for f in os.listdir(pasta) if f.endswith('.xml')]


def ler_arquivo_base64(caminho):
    with open(caminho, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')


def salvar_lote_em_txt(lote, indice_lote):
    conteudo = '[\n' + ',\n'.join(f'"{b64}"' for b64 in lote) + '\n]'
    os.makedirs(PASTA_SAIDA, exist_ok=True)
    nome_arquivo = os.path.join(PASTA_SAIDA, f'lote_{indice_lote:03d}.txt')
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    print(f'Lote {indice_lote:03d} salvo com {len(lote)} XMLs.')


def processar_xmls():
    arquivos = listar_arquivos_xml(PASTA_XML)
    lote = []
    indice_lote = 1

    for i, nome_arquivo in enumerate(arquivos, start=1):
        caminho_arquivo = os.path.join(PASTA_XML, nome_arquivo)
        b64 = ler_arquivo_base64(caminho_arquivo)
        lote.append(b64)

        if len(lote) == LOTE_TAMANHO:
            salvar_lote_em_txt(lote, indice_lote)
            indice_lote += 1
            lote = []

    if lote:
        salvar_lote_em_txt(lote, indice_lote)


processar_xmls()
