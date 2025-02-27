# Autodownloader de Relatórios

Este projeto é um script Python que automatiza o download de relatórios em formato CSV de um site específico(o site utilizado foi o NetSuite) e atualiza uma planilha do Google Sheets com os dados baixados. Esse script é executado em um agendador de tarefas na minha máquina, para automatizar o processo de extração do(s) relatórios.

## Pré-requisitos

- Python 3.x
- Google Chrome
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- Pacotes Python listados em `requirements.txt`

## Instalação

1. Clone este repositório para sua máquina local:

    ```sh
    git clone https://github.com/seu_usuario/autodownloader_relatorios.git
    cd autodownloader_relatorios
    ```

2. Instale os pacotes necessários:

    ```sh
    pip install -r requirements.txt
    ```

3. Configure suas credenciais do Google Cloud Platform (GCP) e baixe o arquivo JSON da conta de serviço.

4. Atualize as variáveis.
    - [user](http://_vscodecontentref_/0)
    - [respostas](http://_vscodecontentref_/1)
    - [url](http://_vscodecontentref_/2)
    - [params](http://_vscodecontentref_/3)
    - [spreadsheet_id](http://_vscodecontentref_/4)
    - e o caminho do arquivo JSON no script [autodownloader_csv.py](http://_vscodecontentref_/5).

## Uso

Execute o script [autodownloader_csv.py](http://_vscodecontentref_/6):

```sh
python autodownloader_csv.py