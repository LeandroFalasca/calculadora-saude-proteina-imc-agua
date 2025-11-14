# Calculadora de Proteína, IMC e Água diária

Projeto em Python para calcular:

- quantidade de proteína diária recomendada
- IMC (Índice de Massa Corporal)
- classificação do IMC
- quantidade de água diária recomendada

## 🎯 Funcionalidades

1. **Calcular Proteína diária (g/dia)**  
   - Usuário escolhe o objetivo:
     - perder peso
     - manter peso
     - ganhar peso
   - O sistema multiplica o peso por um fator (ex: 2g/kg) conforme o objetivo.

2. **Calcular IMC**
   - Fórmula: `IMC = peso / (altura²)`
   - Retorna também a classificação:
     - abaixo do peso
     - peso normal
     - sobrepeso
     - obesidade

3. **Calcular quantidade de água diária**
   - Fórmula: `peso * 35` (ml por kg)
   - Exibe o total recomendado em ml (ou litros, dependendo da versão)

## 🛠 Tecnologias utilizadas

- Python 3
- VS Code

## 📁 Estrutura do projeto

- `funcoes.py`
  - `menu()` → exibe o menu principal
  - `menu_objetivo()` → exibe o menu de objetivos
  - `calc_proteinas(peso, objetivo)`
  - `calc_imc(peso, altura)`
  - `imc(valor_imc)` → retorna a classificação
  - `calc_agua(peso)` → calcula água diária recomendada

- `main.py`
  - Loop principal com `while True`
  - Exibe o menu
  - Lê a opção do usuário
  - Chama as funções corretas
  - Permite sair do sistema digitando uma opção fora do menu

## ▶ Como executar

No terminal:

```bash
python main.py
