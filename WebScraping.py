from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


def EscribirDatos(ListaDatos):
    new_days = open(PATH_CHROME_DRIVER, 'w')
    for i in ListaDatos:
        new_days.write(i)
################### LOG IN ###################


PATH_CHROME_DRIVER = "/Users/lucaswongmang/Downloads/chromedriver"

chromeOptions = webdriver.ChromeOptions()

browser = webdriver.Chrome(executable_path=PATH_CHROME_DRIVER, chrome_options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())

browser.get('https://sfe.bizlinks.com.pe/sfeperu/login.jsf')

#campoRuc = browser.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/div[2]/div/span/div/div[1]/input')
#campoRuc.clear()
#campoRuc.send_keys('20536830376')

campoUsuario = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/div[2]/form/table/tbody/tr[3]/td[2]/input')
campoUsuario.clear()
campoUsuario.send_keys('rsalazar@topsa.com.pe')

campoClave = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/div[2]/form/table/tbody/tr[5]/td[2]/input[1]')
campoClave.clear()
campoClave.send_keys('Psicologia23')

time.sleep(1)

campoClave = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/div[2]/form/table/tbody/tr[9]/td[2]/button')
campoClave.click()

################### SACAR DATOS ###################
time.sleep(5)
ComprobantePagoFact=browser.find_element_by_xpath("/html/body/div[2]/div[2]/form/div/div/div[2]/div[1]/div/ul/li[1]/a")
ComprobantePagoFact.click()

time.sleep(15)
array = []
temparray = []
cont = 0
buscar = browser.find_element_by_xpath('/html/body/div[3]/div/form[1]/div/div[2]/button[1]')
buscar.click()
time.sleep(25)
a = True
counter = 1
contPagina = 2
row = ""
while a == True:
    elen_tabla = browser.find_element_by_xpath('/html/body/div[3]/div/form[2]/div[2]/div[2]/div/div[2]/table/tbody')
    tr_contents = elen_tabla.find_element_by_tag_name('tr')
while a == True:
    elem_tabla = browser.find_element_by_xpath('/html/body/div[3]/div/form[2]/div[2]/div[2]/div/div[2]/table/tbody')
    #tr_contents2 = elem_tabla.find_element_by_tag_name('tbody')
    tr_contents = elem_tabla.find_elements_by_tag_name('tr')
    for tr in tr_contents:
        checkbox = browser.find_element_by_xpath('/html/body/div[3]/div/form[2]/div[2]/div[2]/div/div[2]/table/tbody/tr['+str(counter)+']/td[1]/div/div/div')
        checkbox.click()
        #elem_doc.click()
        #NombreEmpresa = Select(browser.find_element_by_name('ctl00$MainContent$cboDenominacionSocial'))
        #selected_option = NombreEmpresa.first_selected_option.text
        #row = row + "|" + selected_option
        time.sleep(1)
        print("")
        counter += 1
    exportar_Lista = browser.find_element_by_xpath("/html/body/div[3]/div/form[2]/div[1]/div[2]/button")
    #exportar_Lista.click()
    descargarButton = browser.find_element_by_xpath("/html/body/div[3]/div/form[2]/div[1]/div[2]/span[2]/button")
    descargarButton.click()
    registrosSelec = browser.find_element_by_xpath("/html/body/div[15]/ul/li[1]")
    #registrosSelec.click()
    #/html/body/div[3]/div/form[2]/div[1]/div[2]/span[2]/button
    try:
        Pagina = browser.find_element_by_xpath('/html/body/div[3]/div/form[2]/div[2]/div[2]/div/div[3]/div/table/tfoot/tr/td/span[4]/span['+str(contPagina)+']')
        Pagina.click()
        contPagina += 1
        time.sleep(5)
        counter = 1

    except:
        a = False
        print("No se encontró más páginas")




#campoSalir = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[1]/td[4]/table/tbody/tr[1]/td/div/a')
#campoSalir.click()
print("Adios")
