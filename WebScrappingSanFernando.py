from selenium import webdriver
import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

path = "/Users/lucaswongmang/Downloads/Links2.txt"
arrayLinks = []
def extractDoc(url):
    output_dir = '/Users/lucaswongmang/Downloads'
    req = requests.get(url)
    if req.status_code == 200:
        file_path = os.path.join(output_dir, os.path.basename(url))
        with open(file_path, 'wb') as f:
            f.write(req.content)


def DescargarXML(ListaLinks):
    doc = open(path, 'r')
    for i in ListaLinks:
        print(i)
        extractDoc(i)


def EscribirOutput(ListaLinks):
    doc = open(path, 'a')
    for i in ListaLinks:
        doc.write(i + '\n')


def BuscarComponente(browser, path):
    b = True
    cont = 0
    while b == True:
        try:
            componente = browser.find_element_by_xpath(path)
            encontrado = componente.text
            b = False
        except:
            time.sleep(1)
            cont += 1
            if cont > 120:
                print("No se encontró el componente" + str(path))
                print("Iteración N#" + str(cont))
                return False
    return True


def BuscarObjeto(browser, path):
    b = True
    cont = 0
    while b == True:
        try:
            if BuscarComponente(browser, path) == True:
                componente = browser.find_element_by_xpath(path)
                return componente
                b = False
            else:
                b = True
        except:
            time.sleep(1)
            cont += 1
            if cont > 10:
                print("No se encontró el componente" + str(path))
                print("Iteración N#" + str(cont))
                return False


def DarClick(browser, path):
    b = True
    cont = 0
    while b == True:
        try:
            if BuscarComponente(browser, path) == True:
                componente = browser.find_element_by_xpath(path)
                componente.click()
                b = False
            else:
                b = True
        except:
            time.sleep(1)
            cont += 1
            if cont > 10:
                print("No se encontró el componente" + str(path))
                print("Iteración N#" + str(cont))
                return False
    return True

def Delete(browser, path):
    b = True
    cont = 0
    while b == True:
        try:
            if BuscarComponente(browser, path) == True:
                componente = browser.find_element_by_xpath(path)
                componente.click()
                browser.sendKeys(Keys.CONTROL + "a")
                browser.sendKeys(Keys.DELETE)
                b = False
            else:
                b = True
        except:
            time.sleep(1)
            cont += 1
            if cont > 10:
                print("No se pudo hacer DELETE" + str(path))
                print("Iteración N#" + str(cont))
                return False
    return True

def Escribir(browser, path, texto):
    b = True
    cont = 0
    while b == True:
        try:
            if BuscarComponente(browser, path) == True:
                componente = browser.find_element_by_xpath(path)
                componente.clear()
                componente.send_keys(texto)
                b = False
            else:
                b = True
        except:
            time.sleep(1)
            cont += 1
            if cont > 10:
                print("No se encontró el componente" + str(path))
                print("Iteración N#" + str(cont))
                return False
    return True


def ExtraerLink(browser, path):
    b = True
    cont = 0
    while b == True:
        try:
            if BuscarComponente(browser, path) == True:
                componente = browser.find_element_by_xpath(path)
                link = componente.get_attribute("href")
                b = False
                return link
            else:
                b = True
        except:
            time.sleep(1)
            cont += 1
            if cont > 10:
                print("No se encontró el componente" + str(path))
                print("Iteración N#" + str(cont))
                return False


def GenerarBrowser():
    PATH_CHROME_DRIVER = "/Users/lucaswongmang/Downloads/chromedriver"
    #"/Users/lucaswongmang/Desktop/TEC/PwCWebScraping2/chromedriver"
    chromeOptions = webdriver.ChromeOptions()
    #chromeOptions.add_experimental_option("prefs", {
     #   "download.default_directory": "/Users/lucaswongmang/Desktop/TEC/PwCWebScraping2/chromedriver",
    #})
    return webdriver.Chrome(executable_path=PATH_CHROME_DRIVER)



def DescargarFacturas(fechaInicio, FechaFin):
    browser = GenerarBrowser()
    if browser == False:
        print("Error al generar navegador")
        return

    browser.get('https://sanfernando.ecomprobantes.pe/dbnWeb/')

#Usuario
    if Escribir(browser, '/html/body/form/input[1]', 'userSANFERNANDO10') == False:
        print("Error al escribir Usuario")
        return
#Contraseña
    if Escribir(browser, '/html/body/form/input[2]', '12345678') == False:
        print("Error al escribir Contraseña")
        return

    time.sleep(8)
    if DarClick(browser, '/html/body/form/input[3]') == False:
        print("Error al ENTER")
        return
#XXX
    time.sleep(30)
    print("Empieza busqueda")
    elem_xml_1 = browser.find_element_by_xpath("/html/body/form/table[2]/tbody/tr[2]/td/div/div[1]/table/tbody/tr[2]/td[7]/a")
    elem_xml_1.click ()
    a = True
    contDocument = 0
    contPagina = 7
    x = 1
    #while a == True:
    time.sleep(5)
    print("Iteracion de descarga")

    for i in range(2, 202, 1):#502
        #/html/body/form/table[2]/tbody/tr[2]/td/div/div[1]/table/tbody/tr[2]/td[7]/a
        #/html/body/form/table[2]/tbody/tr[2]/td/div/div[1]/table/tbody/tr[2]/td[7]/a/img
        print('/html/body/form/table[2]/tbody/tr[2]/td/div/div[1]/table/tbody/tr[' + str(i) + ']/td[7]/a')
        if DarClick(browser,'/html/body/form/table[2]/tbody/tr[2]/td/div/div[1]/table/tbody/tr[' + str(i) + ']/td[7]/a') == False:
            print("Error al dar descargar archivo")
            continue
        time.sleep(1)

    x += 1
    print("salió del for")
DescargarFacturas('01-01-2021', '31-01-2021')#31

'''
        try:
            print('/html/body/form/div[3]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/input')

            if DarClick(browser, '/html/body/form/div[3]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/input') == False:
                print("Error al dar en cambiar a página: " + str(contPagina))
                a = False
                return

        except:
            a = False
            print("No se encontró más páginas")

    print("Se terminó de descargas las facturasxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


#DescargarFacturas('01-02-2021', '28-02-2021')
#DescargarFacturas('01-03-2021', '31-03-2021')
#DescargarFacturas('01-04-2021', '30-04-2021')
#DescargarFacturas('01-05-2021', '31-05-2021')
#DescargarFacturas('01-06-2021', '30-06-2021')
#DescargarFacturas('01-07-2021', '31-07-2021')
#DescargarFacturas('01-08-2021', '31-08-2021')
#DescargarFacturas('01-09-2021', '30-09-2021')
#DescargarFacturas('01-10-2021', '31-10-2021')
#DescargarFacturas('01-11-2021', '30-11-2021')
#DescargarFacturas('01-12-2021', '31-12-2021')

#XXX

    if DarClick(browser, '/html/body/form/div[3]/div/table[2]/tbody/tr/td[4]/a') == False:
        print("Error al dar Salida CPE")
        return

    if DarClick(browser, '/html/body/form/div[3]/div/div[1]/table[2]/tbody/tr[2]/td[5]/a') == False:
        print("Error al dar click en monitorCPE")
        return

    if DarClick(browser, '/html/body/form/table[2]/tbody/tr[1]/td/div/table/tbody/tr[1]/td[2]/input') == False:
        print("Error al dar click en documentos emitidos")
        return
'''
