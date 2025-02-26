from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import csv
import io
import gspread
from time import sleep
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import AuthorizedSession

options = Options()
options.add_argument('--headless=new')  # Ativa o modo headless (novo padrão para versões recentes do Chrome)
options.add_argument('--disable-gpu')  # Desativa a GPU para evitar problemas em ambientes headless
options.add_argument('--window-size=1920x1080')  # Define o tamanho da janela no modo headless

user = {
    'email':'seu_email@gmail.com',
    'password':'Senha123'
}
respostas = {
    'Pergunta1?':'resposta1',
    'Pergunta2?':'resposta2',
    'Pergunta3?':'resposta3'
}
driver = webdriver.Chrome(options=options)

# Accessing Netsuite

driver.get('Link do site')
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(user['email'])
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(user['password'])
driver.find_element(By.XPATH, '//*[@id="login-submit"]').click()

# Safety Ask Validation

elements = driver.find_elements(By.CSS_SELECTOR, 'td.smalltextnolink.text-opensans')

text = elements[2].text  # Get the text of the third element (0-based index)

resposta = respostas.get(text)
driver.find_element(By.XPATH, '//*[@id="null"]').send_keys(resposta)
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/table/tbody/tr[4]/td/input').click()

cookie = driver.get_cookie('JSESSIONID')

sleep(20)

url = 'URL de download do CSV'
params = {
    'param1': 'value1',
    'param2':'value2',
    'param3':'value3',
    'param4':'value4'

}
headers = {
    'cookie': 'JSESSIONID={};'.format(cookie.get('value')),
}

data_list = []

try:
    response = requests.get(url, params=params, headers=headers, verify=False)
    response.raise_for_status()  # Check for HTTP errors
    pedidos = response.text

    # Parse CSV content
    csv_reader = csv.reader(io.StringIO(pedidos))
    for row in csv_reader:
        data_list.append(row)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(r"Caminho do JSON do GCP", scopes=scope)
session = AuthorizedSession(creds)
session.verify = False


client = gspread.authorize(creds, session=session)

# Open the Google Sheet by title or ID
spreadsheet_id = 'ID da Planilha'  # replace with your actual Google Sheet ID
sheet = client.open_by_key(spreadsheet_id).sheet1  # Replace 'sheet1' if accessing a different sheet/tab
sheet.clear()
# Update a cell (e.g., cell A1) with new data
sheet.update(range_name='A1', values=data_list)

print('Spreadsheet updated successfully!')
