import os
import pandas as pd

PASTA_EXTRACTED = "data/extracted"
PALAVRAS_CHAVE = [
    "EVENTO",
    "SINISTRO",
    "ASSISTENCIAL",
    "ASSISTENCIA"
]


def eh_despesa(descricao):
    if pd.isna(descricao):
        return False
    descricao = str(descricao).upper()
    return any(p in descricao for p in PALAVRAS_CHAVE)


def processar_csv(caminho_csv, ano, trimestre):
    df = pd.read_csv(caminho_csv, sep=";", encoding="latin1")

    # filtra apenas linhas de despesas
    df_despesas = df[df["DESCRICAO"].apply(eh_despesa)].copy()

    if df_despesas.empty:
        return pd.DataFrame()

    df_despesas["Ano"] = ano
    df_despesas["Trimestre"] = trimestre
    df_despesas["ValorDespesas"] = df_despesas["VL_SALDO_FINAL"]

    return df_despesas[[
        "REG_ANS",
        "DESCRICAO",
        "Ano",
        "Trimestre",
        "ValorDespesas"
    ]]


def main():
    todos = []

    for pasta in os.listdir(PASTA_EXTRACTED):
        caminho_pasta = os.path.join(PASTA_EXTRACTED, pasta)

        if not os.path.isdir(caminho_pasta):
            continue

        # pasta no formato: 2025_3T
        ano, tri = pasta.split("_")
        trimestre = int(tri.replace("T", ""))

        for arquivo in os.listdir(caminho_pasta):
            if arquivo.lower().endswith(".csv"):
                caminho_csv = os.path.join(caminho_pasta, arquivo)
                df = processar_csv(caminho_csv, int(ano), trimestre)

                if not df.empty:
                    todos.append(df)

    if not todos:
        print("Nenhuma despesa encontrada.")
        return

    consolidado = pd.concat(todos, ignore_index=True)

    print("Resumo das despesas encontradas:")
    print(consolidado.head())
    print(f"\nTotal de registros: {len(consolidado)}")
    os.makedirs("output", exist_ok=True)

    consolidado.to_csv(
        "output/consolidado_despesas.csv",
        index=False,
        sep=";",
        encoding="utf-8"
    )


if __name__ == "__main__":
    main()
