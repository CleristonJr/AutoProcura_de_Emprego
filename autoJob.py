from selenium import webdriver
import pyautogui as pag
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()

# Inicializa o navegador
driver = webdriver.Chrome()

# Acessa uma página web
driver.get("https://www.infojobs.com.br/vagas-de-emprego-help-trabalho-home-office.aspx")

try:
    # Espera até que o botão de aviso esteja presente e visível
    agree_button = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
    )
    agree_button.click()
    encontrou = 'true'
except:
    encontrou = 'false'

# Cria e escreve no arquivo TXT
with open("resultado_busca.txt", "w") as file:
    file.write(f"Botão de aviso encontrado: {encontrou}\n")

try:
    # Espera até que os elementos <a> com as classes concatenadas especificadas estejam presentes
    link_elements = WebDriverWait(driver, 120).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".d-flex .mr-8 .text-decoration-none"))
    )

    # Limita o número de links de 2 a 5
    min_links = 2
    max_links = 5
    link_elements = link_elements[:max_links] if len(link_elements) >= max_links else link_elements[:min_links]

    # Obtém os valores dos atributos href
    link_hrefs = [link.get_attribute("href") for link in link_elements]

    # Escreve no arquivo TXT
    with open("resultado_busca.txt", "a") as file:  # Use "a" para anexar ao arquivo existente
        for idx, href in enumerate(link_hrefs, start=1):
            file.write(f"Link {idx}: {href}\n")
        file.write("Busca realizada: Selenium WebDriver\n")

except Exception as e:
    with open("resultado_busca.txt", "w") as file:
        file.write("erro ao encontrar os links")


# Abra o arquivo em modo de leitura (r)
with open('resultado_busca.txt', 'r') as arquivo:
    # Leia todas as linhas do arquivo
    linhas = arquivo.read()

# Exiba cada linha


'''
time.sleep(3)
pag.press('win')
pag.write('Whatsapp')
pag.press('enter')
time.sleep(3)
pag.write('Eu Eu Mesmo')
pag.press('tab')
pag.press('enter')
time.sleep(3)
localMensagem = pag.locateCenterOnScreen('mensagem.png', confidence = 0.9)
pag.click(localMensagem)
time.sleep(3)
pag.write(linhas, interval=0.1)

    #print(conteudo)

    # Fecha o navegador
    #driver.quit()

    
'''
