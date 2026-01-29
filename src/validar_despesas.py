import pandas as pd
import os

CAMINHO_INPUT = "output/consolidado_despesas.csv"
CAMINHO_OUTPUT = "output/consolidado_despesas_validado.csv"


def converter_valor(valor):
    """
    Converte valores no formato brasileiro (1.234,56) para float.
    """
    if pd.isna(valor):
        return None

    try:
        valor = str(valor).replace(".", "").replace(",", ".")
        return float(valor)
    except ValueError:
        return None


def main():
    df = pd.read_csv(CAMINHO_INPUT, sep=";", encoding="utf-8")

    # remove REG_ANS inválido
    df = df[df["REG_ANS"].notna()]

    # converte valor
    df["ValorNumerico"] = df["ValorDespesas"].apply(converter_valor)

    # remove valores inválidos
    df = df[df["ValorNumerico"].notna()]

    # marca valores zerados
    df["ValorZerado"] = df["ValorNumerico"] == 0

    # remove valores negativos
    df = df[df["ValorNumerico"] >= 0]

    os.makedirs("output", exist_ok=True)

    df.to_csv(
        CAMINHO_OUTPUT,
        index=False,
        sep=";",
        encoding="utf-8"
    )

    print("Validação concluída")
    print(f"Registros finais: {len(df)}")
    print(df.head())


if __name__ == "__main__":
    main()
