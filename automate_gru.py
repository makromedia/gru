from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import sys

def preencher_gru(data):
    # Configurações do Selenium Grid
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://pagtesouro.tesouro.gov.br/portal-gru/#/emissao-gru/formulario')

        # Preencher a primeira etapa
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'ug')))
        driver.find_element(By.NAME, 'ug').send_keys(data['ug'])
        driver.find_element(By.NAME, 'codigoRecolhimento').send_keys(data['codigo_recolhimento'])
        driver.find_element(By.XPATH, '//button[text()="Avançar"]').click()

        # Preencher a segunda etapa
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'cpfCnpjContribuinte')))
        driver.find_element(By.NAME, 'cpfCnpjContribuinte').send_keys(data['cpf_cnpj'])
        driver.find_element(By.NAME, 'nomeContribuinte').send_keys(data['nome_contribuinte'])
        driver.find_element(By.NAME, 'numeroReferencia').send_keys(data['referencia'])
        driver.find_element(By.NAME, 'competencia').send_keys(data['competencia'])
        driver.find_element(By.NAME, 'vencimento').send_keys(data['vencimento'])
        driver.find_element(By.NAME, 'valorPrincipal').send_keys(data['valor_principal'])

        # Submeter o formulário
        driver.find_element(By.XPATH, '//button[text()="Emitir GRU"]').click()

        # Esperar um pouco para garantir que o processo foi concluído
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[text()="GRU Emitida"]')))

    finally:
        driver.quit()

if __name__ == "__main__":
    data = json.loads(sys.argv[1])
    preencher_gru(data)
