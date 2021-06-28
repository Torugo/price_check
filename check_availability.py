from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


import chromedriver_binary
from icecream import ic
# wd.implicity_wait()
lojas = ['americanas', 'magalu', 'ponto']
s21plus = {'americanas' : 'https://www.americanas.com.br/produto/2833430945?pfm_carac=s21&pfm_index=7&pfm_page=search&pfm_pos=grid&pfm_type=search_page&cor=PRETO',
                  'magalu': 'https://www.magazineluiza.com.br/smartphone-samsung-galaxy-s21-256gb-preto-5g-8gb-ram-tela-67-cam-tripla-selfie-10mp/p/155620100/te/tcsp/',
                  'ponto': 'https://www.pontofrio.com.br/TelefoneseCelulares/Smartphones/Android/smartphone-samsung-galaxy-s21-5g-preto-256gb-8gb-ram-tela-infinita-de-6-7-camera-traseira-tripla-android-11-e-processador-octa-core-55018615.html?IdSku=55018615'}

s21 = {'americanas' : 'https://www.americanas.com.br/produto/2875240373?pfm_carac=s21&pfm_index=1&pfm_page=search&pfm_pos=grid&pfm_type=search_page&cor=CINZA'}



elements = {'americanas':  """//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[2]/div""", 
            'magalu': """/html/body/div[3]/div[5]/div[1]/div[3]/div[2]/div[6]/div/div[2]/div/span[2]""",
            'ponto': """//*[@id="product-price-box"]/p"""}

wd = wd.Chrome()
for loja in lojas:
    wd.get(s21plus[loja])
    try:
            element = WebDriverWait(wd,50).until(
                    ec.presence_of_element_located((By.XPATH,elements[loja])))
    except Exception as e:
        ic(e)
        ic('caught exception closing browser')
        wd.quit()
    # WebDriverWait(wd, 20)
    preco = wd.find_element_by_xpath(elements[loja]).text
    ic(preco)