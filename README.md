# Teste de Nivelamento – Estágio IntuitiveCare 2026

Este repositório contém a solução para o teste de nivelamento técnico proposto pela IntuitiveCare.
A solução foi desenvolvida em Python, com foco em clareza, organização, resiliência a dados reais
e decisões técnicas bem justificadas.

---

## 📋 O Que o Teste Pede

Este teste tem os seguintes objetivos:
```
1. Acessar o repositório público da ANS e identificar os trimestres mais recentes.
2. Baixar, extrair e consolidar demonstrações contábeis.
3. Identificação e extração de despesas relacionadas a eventos/sinistros.
4. Validação e normalização dos dados.
5. Entregar arquivos `.csv` consolidados prontos para análise.
```
Além disso, são avaliados:
```
- Clareza e organização do código;
- Justificativas técnicas;
- Boas práticas de programação;
- Documentação explicativa.
```

## 🧾 Resultados Alcançados
```
 Requisito                                    Status      
| Identificar trimestres mais recentes | ✅ Concluído |
| Baixar e extrair ZIPs                | ✅ Concluído |
| Consolidar despesas em CSV           | ✅ Concluído |
| Normalizar e validar dados           | ✅ Concluído |
| Geração de CSV final validado        | ✅ Concluído |
```

## 📌 Visão Geral da Solução

O projeto implementa um pipeline completo para:

1. Acessar os dados públicos da ANS (FTP)
2. Identificar automaticamente os três trimestres mais recentes disponíveis
3. Baixar e extrair os arquivos de demonstrações contábeis
4. Identificar e processar despesas relacionadas a eventos/sinistros
5. Consolidar os dados em um único arquivo CSV
6. Validar e normalizar os dados consolidados

Todo o fluxo foi pensado para lidar com estruturas inconsistentes, diferentes formatos de dados
e grande volume de registros.

---

teste-intuitive-care/
```
│
├── data/
│ ├── raw/ # Arquivos ZIP baixados da ANS
│ └── extracted/ # Conteúdo extraído por ano/trimestre
│
├── output/
│ ├── consolidado_despesas.csv
│ └── consolidado_despesas_validado.csv
│
├── src/
│ ├── coletar_trimestres.py
│ ├── baixar_zips.py
│ ├── extrair_zips.py
│ ├── identificar_despesas.py
│ ├── mapear_arquivos.py
│ ├── processar_despesas.py
│ └── validar_despesas.py
│
├── requirements.txt
└── README.md
```

## 🗂️ Estrutura do Projeto

---

## ▶️ Como Executar
  
### 1️⃣ Criar ambiente virtual 
```
python -m venv venv
```
2️⃣ Ativar o ambiente

Windows
```
venv\Scripts\activate
```

3️⃣ Instalar dependências
```
pip install -r requirements.txt
```

4️⃣ Executar o pipeline (ordem recomendada)
```
python src/coletar_trimestres.py
python src/baixar_zips.py
python src/extrair_zips.py
python src/processar_despesas.py
python src/validar_despesas.py
```

🧠 Decisões Técnicas e Trade-offs

🔹 Identificação dos Trimestres

Os trimestres não seguem uma estrutura fixa de diretórios na ANS.
A solução identifica os períodos dinamicamente a partir do nome dos arquivos ZIP
```(padrão <trimestre>T<ano>)```, tornando o processo resiliente a variações estruturais.

🔹 Processamento Incremental

Os arquivos são processados de forma incremental, evitando o carregamento
de grandes volumes de dados simultaneamente em memória.

🔹 Identificação de Despesas

Os arquivos não possuem uma coluna explícita chamada “Despesa”.
As despesas com eventos/sinistros foram identificadas a partir da coluna DESCRICAO,
utilizando palavras-chave relacionadas ao domínio contábil
(eventos, sinistros, assistência).

🔹 Encoding

Os arquivos de origem utilizam encoding Latin-1.
Os dados foram lidos nesse formato e exportados em UTF-8.
Eventuais caracteres especiais inconsistentes não afetam o valor semântico dos dados.

🔹 Tratamento de Valores Monetários

Os valores monetários estavam no formato brasileiro (1.234,56).
Eles foram convertidos para valores numéricos (float) durante a etapa de validação.

✔️ Validações Aplicadas
```
Registros com REG_ANS nulo foram descartados

Valores monetários inválidos ou não numéricos foram descartados

Valores negativos foram descartados

Valores zerados foram mantidos e sinalizados

Essas decisões priorizam a integridade dos dados para análises financeiras futuras.
```

📊 Resultado Final
```
Arquivo consolidado: output/consolidado_despesas.csv

Arquivo validado: output/consolidado_despesas_validado.csv

Total de registros processados: ~248 mil
```
📝 Considerações Finais
```
A solução foi desenvolvida priorizando:

Clareza e organização do código

Tratamento de dados reais e inconsistentes

Justificativas técnicas explícitas

Simplicidade (KISS) sem perder robustez

O projeto pode ser facilmente estendido para:

Integração com banco de dados

Exposição via API

Visualização em interface web
```

