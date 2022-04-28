# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import pandas as pd

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\Drivers\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)


driver.get('https://weather.com/')
time.sleep(2)
WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[1]/header/div/div[2]/div[1]/div/div[1]/input')))\
    .send_keys('Santiago de Chile')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/header/div/div[2]/div[1]/div/div[1]/input').send_keys(Keys.ENTER)
time.sleep(2)
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div[3]/div[3]/div/nav/div/div[1]/a[2]')))\
    .click()
time.sleep(2)
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#detailIndex0 > summary > div > svg')))\
    .click()
time.sleep(2)
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]')))
texto_columnas3 = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]')
texto_columnas3 = texto_columnas3.text
tiempo_hoy3 = texto_columnas3.split('23:00')[0].split('\n')[1:-1]

hora3 = list()
temp3 = list()
calidad3 = list()
proba_lluvia3 = list()
v_viento3 = list()

for j in range(0,len(tiempo_hoy3),5):
    hora3.append(tiempo_hoy3[j])
    temp3.append(tiempo_hoy3[j+1])
    calidad3.append(tiempo_hoy3[j+2])
    proba_lluvia3.append(tiempo_hoy3[j+3])
    v_viento3.append(tiempo_hoy3[j+4])

df3 = pd.DataFrame({'Hora' : hora3, 'Temperatura' : temp3, 'Tiempo' : calidad3, 'Probabilidad lluvia' : proba_lluvia3, 'Velocidad viento' : v_viento3})
print('El tiempo por hora en weather.com')
print(df3)
driver.quit()
