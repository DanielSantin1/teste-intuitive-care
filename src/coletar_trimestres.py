import re
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"


def listar_links(url):
    """
    Acessa uma URL da ANS e retorna todos os links encontrados na página.
    """
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    return [a.get("href") for a in soup.find_all("a") if a.get("href")]


def obter_anos():
    """
    Retorna uma lista de anos disponíveis (ex: 2023, 2024, 2025).
    """
    links = listar_links(BASE_URL)
    anos = []

    for link in links:
        nome = link.strip("/")
        if nome.isdigit() and len(nome) == 4:
            anos.append(int(nome))

    return sorted(anos)


def extrair_ano_trimestre(nome_arquivo):
    """
    Extrai o ano e o trimestre do nome do arquivo ZIP.
    Exemplo:
    - 1T2024.zip        -> ano=2024, trimestre=1
    - 20130416_1T2012.zip -> ano=2012, trimestre=1
    """
    match = re.search(r"([1-4])T(\d{4})", nome_arquivo)
    if match:
        trimestre = int(match.group(1))
        ano = int(match.group(2))
        return ano, trimestre

    return None, None


def coletar_trimestres():
    """
    Percorre todos os anos e coleta todos os arquivos ZIP
    que representam trimestres contábeis.
    """
    resultados = []
    anos = obter_anos()

    for ano in anos:
        url_ano = f"{BASE_URL}{ano}/"

        try:
            links = listar_links(url_ano)
        except Exception:
            continue

        for link in links:
            if not link.lower().endswith(".zip"):
                continue

            ano_zip, trimestre = extrair_ano_trimestre(link)

            if ano_zip is not None and trimestre is not None:
                resultados.append(
                    {
                        "ano": ano_zip,
                        "trimestre": trimestre,
                        "arquivo": link,
                        "url": f"{url_ano}{link}",
                    }
                )

    return resultados


def selecionar_trimestres_recentes(qtd=3):
    """
    Seleciona os N trimestres mais recentes com base em ano e trimestre.
    """
    trimestres = coletar_trimestres()

    trimestres_ordenados = sorted(
        trimestres,
        key=lambda x: (x["ano"], x["trimestre"]),
        reverse=True,
    )

    return trimestres_ordenados[:qtd]


if __name__ == "__main__":
    recentes = selecionar_trimestres_recentes()

    print("3 trimestres mais recentes encontrados:")
    for r in recentes:
        print(r)
