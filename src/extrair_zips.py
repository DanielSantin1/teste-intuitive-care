import os
import zipfile
from coletar_trimestres import selecionar_trimestres_recentes

PASTA_RAW = "data/raw"
PASTA_EXTRACTED = "data/extracted"


def garantir_pastas():
    if not os.path.exists(PASTA_EXTRACTED):
        os.makedirs(PASTA_EXTRACTED)


def extrair_zip(caminho_zip, destino):
    with zipfile.ZipFile(caminho_zip, "r") as zip_ref:
        zip_ref.extractall(destino)


def main():
    garantir_pastas()

    trimestres = selecionar_trimestres_recentes()

    for t in trimestres:
        nome_zip = t["arquivo"]
        ano = t["ano"]
        trimestre = t["trimestre"]

        caminho_zip = os.path.join(PASTA_RAW, nome_zip)
        pasta_destino = os.path.join(PASTA_EXTRACTED, f"{ano}_{trimestre}T")

        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        print(f"📦 Extraindo {nome_zip} para {pasta_destino}")
        extrair_zip(caminho_zip, pasta_destino)


if __name__ == "__main__":
    main()
