# BCP DTVM - Processo Seletivo

Este repositório contém a solução para o desafio de programação proposto no processo seletivo da BCP DTVM. O objetivo é desenvolver um script em Python para automatizar a conferência de registros de negociações de debêntures, comparando dados internos com informações públicas da ANBIMA.

## 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma:

```bash
├── main.py                                   # Script principal
├── README.md
├── scr/
│   └── functions.py                          # Funções auxiliares (leitura, busca na API, comparação)
│
├── inputs/                                   # Dados internos
│   └── Registros_BCPSA4.csv
└── outputs/                                  # Arquivos gerados
    ├── Negociacoes_BCPSA4.csv
    └── Divergencias_Negociacoes_BCPSA4.csv         
```

## ▶️ Configuração do Ambiente

Antes de executar, crie um ambiente virtual (venv). Certifique-se de ter o Python (3.12.3) instalado.
1.  **Crie um ambiente virtual, digite no terminal:**
    ```bash
    python -m venv venv
    ```

2.  **Ative o ambiente virtual:**
    *   No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Instale as dependências necessárias:**
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Como Executar

Com o ambiente configurado e as dependências instaladas, basta executar o script principal a partir da raiz do projeto:

```bash
python main.py
```

Ao final da execução, os arquivos Negociacoes_BCPSA4.csv e Divergencias_Negociacoes_BCPSA4.csv serão criados ou atualizados no diretório outputs/.

#
## 👨‍💻 Autor
* João Fernando
* LinkedIn: https://www.linkedin.com/in/joaoffialho/