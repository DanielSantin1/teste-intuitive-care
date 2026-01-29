import os

PASTA_EXTRACTED = "data/extracted"

PALAVRAS_CHAVE = [
    "DESPESA",
    "EVENTO",
    "SINISTRO"
]


def eh_arquivo_despesa(nome_arquivo):
    nome_upper = nome_arquivo.upper()
    return any(palavra in nome_upper for palavra in PALAVRAS_CHAVE)


def localizar_arquivos_despesa():
    arquivos_encontrados = []

    for raiz, _, arquivos in os.walk(PASTA_EXTRACTED):
        for arquivo in arquivos:
            if eh_arquivo_despesa(arquivo):
                caminho_completo = os.path.join(raiz, arquivo)
                arquivos_encontrados.append(caminho_completo)

    return arquivos_encontrados


if __name__ == "__main__":
    arquivos = localizar_arquivos_despesa()

    print("Arquivos de despesas encontrados:")
    for a in arquivos:
        print(a)

    print(f"\nTotal: {len(arquivos)} arquivos")
