import os
import requests
from coletar_trimestres import selecionar_trimestres_recentes

PASTA_RAW = "data/raw"


def garantir_pasta():
    if not os.path.exists(PASTA_RAW):
        os.makedirs(PASTA_RAW)


def baixar_zip(url, caminho_destino):
    print(f"⬇️  Baixando {url}")
    resposta = requests.get(url, stream=True)
    resposta.raise_for_status()

    with open(caminho_destino, "wb") as arquivo:
        for chunk in resposta.iter_content(chunk_size=8192):
            arquivo.write(chunk)


def main():
    garantir_pasta()

    trimestres = selecionar_trimestres_recentes()

    for t in trimestres:
        nome_arquivo = t["arquivo"]
        url = t["url"]
        destino = os.path.join(PASTA_RAW, nome_arquivo)

        if os.path.exists(destino):
            print(f"✔️ Já existe: {nome_arquivo}")
            continue

        baixar_zip(url, destino)


if __name__ == "__main__":
    main()
