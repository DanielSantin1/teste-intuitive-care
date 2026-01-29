import os
import csv

PASTA_EXTRACTED = "data/extracted"


def listar_arquivos():
    arquivos = []

    for raiz, _, files in os.walk(PASTA_EXTRACTED):
        for f in files:
            arquivos.append(os.path.join(raiz, f))

    return arquivos


def inspecionar_csv(caminho):
    try:
        with open(caminho, encoding="latin1") as f:
            reader = csv.reader(f, delimiter=";")
            return next(reader)
    except Exception:
        return []


if __name__ == "__main__":
    arquivos = listar_arquivos()

    print(f"Total de arquivos encontrados: {len(arquivos)}\n")

    for a in arquivos:
        ext = os.path.splitext(a)[1].lower()
        print(f"Arquivo: {a}")

        if ext == ".csv":
            colunas = inspecionar_csv(a)
            print("  Colunas:", colunas)

        else:
            print("  (formato não CSV)")

        print("-" * 60)
