# Leitor de músicas em CSV (Python)

Projeto desenvolvido durante o bootcamp de Análise de Dados (Generation Brasil), com o objetivo de praticar leitura de arquivos CSV usando Python.

## 🎯 Objetivo

Ler um arquivo `musicas.csv` contendo informações de músicas (título, artista, ano, gênero e duração) e exibir cada registro formatado no terminal.

## 🛠 Tecnologias utilizadas

- Python 3
- Módulo padrão `csv`
- VS Code

## 📁 Estrutura do projeto

- `funcoes.py` → contém a função `ler_musicas()`, responsável por:
  - abrir o arquivo CSV
  - pular o cabeçalho com `next()`
  - ler linha a linha com `csv.reader`
  - imprimir as informações de forma organizada

- `main.py` → arquivo principal que:
  - importa a função `ler_musicas`  
  - executa a leitura do arquivo ao rodar o script

- `musicas.csv` → base de dados com as músicas utilizadas no exercício.

## ▶ Como executar

1. Certifique-se de que todos os arquivos estejam na mesma pasta.
2. No terminal, navegue até a pasta do projeto.
3. Execute:

```bash
python main.py
