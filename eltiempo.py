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



# Inicializamos el navegador
driver.get('https://www.accuweather.com/')
time.sleep(1)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#privacy-policy-banner > div > div')))\
    .click()

WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[1]/div[3]/div[1]/form/input')))\
    .send_keys('Santiago de')
time.sleep(1)

driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div[1]/form/input').send_keys(Keys.ENTER)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[4]/div[1]/div[1]/div[1]/a[1]')))\
    .click()
time.sleep(2)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

driver.get('https://www.accuweather.com/es/cl/santiago/60449/weather-forecast/60449')
time.sleep(2)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[3]/div/div[3]/a[2]')))\
    .click()
time.sleep(2)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div/div[3]')))\
    .click()
time.sleep(2)

texto_columnas = driver.find_element_by_xpath('/html/body/div/div[5]/div[1]')
texto_columnas = texto_columnas.text
tiempo_hoy = texto_columnas.split('PREVISIÓN FUTURA')[0].split('\n')[0:-1]

hora = list()
temp = list()
cali = list()
proba_lluvia = list()

for j in range(0,len(tiempo_hoy),5):
    hora.append(tiempo_hoy[j] +':00')
    temp.append(tiempo_hoy[j+1])
    cali.append(tiempo_hoy[j+3])
    proba_lluvia.append((tiempo_hoy[j+4]))


df = pd.DataFrame({'Hora': hora, 'Temperatura': temp, 'Calidad': cali, 'Probabilidad lluvia' : proba_lluvia})
print('El tiempo por hora en Accuweather')
print(df)
df.to_csv('tiempo_por_hoy_accu.csv',index=False)
time.sleep(2)

print('----------------------------')
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])

driver.get('https://eltiempo.es')
time.sleep(2)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#didomi-notice-agree-button')))\
    .click()

WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input#term')))\
    .send_keys('Chile')
time.sleep(2)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[5]/nav/div[2]/div[1]/div[3]/div[1]/div[1]/form/label/button/i')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[5]/main/div[4]/div/section[2]/section/div/ul/li[3]/a')))\
    .click()
time.sleep(2)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[5]/main/div[4]/div/section[4]/section/div/article/section/ul/li[2]/h2/a')))\
    .click()
time.sleep(2)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//html/body/div[5]/main/div[4]/div/section[4]/section/div[1]/ul/li[1]/ul')))

time.sleep(2)

texto_columnas2 = driver.find_element_by_xpath('/html/body/div[5]/main/div[4]/div/section[4]/section/div[1]/ul/li[1]/ul')
texto_columnas2 = texto_columnas2.text
array_items = texto_columnas2.split('Mañana')[0].split('\n')
tiempo_hoy2 = array_items[1:len(array_items)]
tiempo_filtrado = list()

for element in tiempo_hoy2:
    if element != 'Temperatura' and element!= 'Previsión' and element != 'Dirección del viento':
        tiempo_filtrado.append(element)

hora2 = list()
temp2 = list()
v_viento2 = list()

for t in range(0,len(tiempo_filtrado),4):
    hora2.append(tiempo_filtrado[t] + ':00')
    temp2.append(tiempo_filtrado[t+1] + 'C')
    v_viento2.append(tiempo_filtrado[t+2] + ' km/h')

df2 = pd.DataFrame({'Hora': hora2, 'Temperatura': temp2, 'Velocidad del viento': v_viento2})
print('El tiempo por hora en eltiempo.es')
print(df2)
df2.to_csv('tiempo_por_hoy_tiempoes.csv',index=False)

print('----------------------------')
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[3])

driver.get('https://www.tutiempo.net/')
time.sleep(2)

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#DivAceptarCookies > div > a:nth-child(5)')))\
    .click()
time.sleep(2)

WebDriverWait(driver,10)\
    .until(EC.element_to_be_clickable((By.XPATH,'//html/body/div[3]/div/form/input')))\
    .send_keys('Santiago')
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[3]/div/form/input').send_keys(Keys.ENTER)
time.sleep(2)


WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[4]/div[5]/div[1]/div/p[2]/a[9]')))\
    .click()
time.sleep(2)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[4])

driver.get('https://www.tutiempo.net/santiago.html')
time.sleep(2)

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[4]/div[5]/div[1]/div/div[4]/div[2]')))
time.sleep(2)

texto_columnas3 = driver.find_element_by_xpath('/html/body/div[4]/div[5]/div[1]/div/div[4]/div[2]')
texto_columnas3 = texto_columnas3.text

#Hora actual + 1 de diferencia
time_hour = (time.localtime().tm_hour+1)

# Se convierte time_hour a string y se le agrega el :00
time_hour_1 = str(time_hour) + ':00'

# Se reemplaza el valor de Ahora por time_hour_1

texto_columnas3 = texto_columnas3.replace('Ahora',time_hour_1)
tiempo_hoy3 = texto_columnas3.split('Hora a hora')[0].split('\n')[0:-1]

hora3 = list()
temp3 = list()
v_viento3= list()

for z in range(0,len(tiempo_hoy3),3):
    hora3.append(tiempo_hoy3[z])
    temp3.append(tiempo_hoy3[z+1])
    v_viento3.append(tiempo_hoy3[z+2])

df3 = pd.DataFrame({'Hora' : hora3, 'Temperatura' : temp3, 'Velocidad viento' : v_viento3})
print('El tiempo por hora en tutiempo.net')
print(df3)
df3.to_csv('tiempo_por_hoy_tutiemponet.csv',index=False)
driver.quit()
