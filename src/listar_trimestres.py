import requests
from bs4 import BeautifulSoup

URL_BASE = "https://dadosabertos.ans.gov.br/FTP/PDA/"

def listar_trimestres():
    response = requests.get(URL_BASE)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    links = [
        a.get("href")
        for a in soup.find_all("a")
        if a.get("href") and a.get("href").endswith("/")
    ]

    links = [l for l in links if l != "../"]

    return links


if __name__ == "__main__":
    trimestres = listar_trimestres()
    print("Diretórios encontrados:")
    for t in trimestres:
        print(t)
