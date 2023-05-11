from selenium import webdriver
import time
import os
import requests
from selenium import webdriver
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
    try:
        PATH_CHROME_DRIVER = "/Users/lucaswongmang/Downloads/chromedriver"
        #"/Users/lucaswongmang/Desktop/TEC/PwCWebScraping2/chromedriver"
        chromeOptions = webdriver.ChromeOptions()
        #chromeOptions.add_experimental_option("prefs", {
         #   "download.default_directory": "/Users/lucaswongmang/Desktop/TEC/PwCWebScraping2/chromedriver",
        #})
        return webdriver.Chrome(executable_path=PATH_CHROME_DRIVER, chrome_options=chromeOptions,
                                desired_capabilities=chromeOptions.to_capabilities())
    except:
        return False


def DescargarFacturas(fechaInicio, FechaFin):
    browser = GenerarBrowser()
    if browser == False:
        print("Error al generar navegador")
        return

    browser.get('http://asp403r.paperless.com.pe/Facturacion/login.jsp?error=Su%20session%20ha%20expirado')

    if Escribir(browser, '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/input', '20600131363') == False:
        print("Error al escribir RUC")
        return

    if Escribir(browser, '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[3]/td[2]/input', 'usuario1') == False:
        print("Error al escribir usuario")
        return

    if Escribir(browser, '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td[2]/input[1]', 'abc123') == False:
        print("Error al escribir clave")
        return
    time.sleep(2)
    if DarClick(browser, '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[5]/td/input') == False:
        print("Error al dar click en enter")
        return

    if DarClick(browser, '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[3]/a') == False:
        print("Error al dar click en gestión documental")
        return

    if DarClick(browser, '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[1]/a') == False:
        print("Error al dar click en documentos emitidos")
        return
    if DarClick(browser, '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/div/form[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/input[1]') == False:
        print("Error al dar click en TODOS")
        return
    if DarClick(browser, '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/div/form[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/input[1]') == False:
        print("Error al dar click en TODOS menos Validos")
        return
    #if DarClick(browser, '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/div/form[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/input[2]') == False:
    #    print("Error al dar click en Validos")
    #    return
    if Escribir(browser, '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/div/form[1]/table/tbody/tr[3]/td[3]/table/tbody/tr[10]/td/input[1]', fechaInicio) == False:
        print("Error al escribir fecha inicio")
        return

    if Escribir(browser,'/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/div/form[1]/table/tbody/tr[3]/td[3]/table/tbody/tr[10]/td/input[2]',FechaFin) == False:
        print("Error al escribir fecha fin")
        return

    if DarClick(browser, '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/div/form[1]/input[2]') == False:
        print("Error al dar click en buscar facturas por rango")
        return

    if DarClick(browser,'/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table[2]/tbody/tr/td[2]/a[5]') == False:
        print("Error al dar click en visualizar 500")
        return

    #if DarClick(browser,'/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table[1]/tbody/tr/td[2]/a[14]') == False:
    #    print("Error al dar click en visualizar 10mo elemnto")
    #    return

    a = True
    contDocument = 0
    contPagina = 6
    x = 1
    while a == True:
        for i in range(2, 502, 1):#502
            if DarClick(browser,'/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/form[1]/table/tbody/tr[' + str(i) + ']/td[12]/a[3]') == False:
                print("Error al dar descargar archivo")
                continue

        #/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/form[1]/table/tbody/tr[2]/td[12]/a[3]
        #/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/form[1]/table/tbody/tr[3]/td[12]/a[3]
        #/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table[1]/tbody/tr/td[2]/a[6]
        x += 1
        print("salió del for")
        try:
            print('/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table[1]/tbody/tr/td[2]/a[' + str(contPagina) + ']')
            #/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table[1]/tbody/tr/td[2]/a[6]
            #/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table[2]/tbody/tr/td[2]/a[7]
            if DarClick(browser, '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table[2]/tbody/tr/td[2]/a[' + str(contPagina) + ']') == False:
                print("Error al dar en cambiar a página: " + str(contPagina))
                a = False
                return
            if x == 11:
                x = 1
                contPagina = 6
            print(contPagina)
            EscribirOutput(arrayLinks)
            contPagina += 1

        except:
            a = False
            print("No se encontró más páginas")

    print("Culminé")

    if DarClick(browser, '/html/body/table[1]/tbody/tr[1]/td[4]/table/tbody/tr[1]/td/div/a') == False:
        print("Error al dar click en salir")
        return

    print("Se terminó de descargas las facturasxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

#DescargarFacturas('01-01-2021', '31-01-2021')#31
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
DescargarFacturas('01-12-2021', '31-12-2021')

#30
#31
#file1 = open(path, 'r')
#Lines = file1.readlines()
#DescargarXML(Lines)
# 5971
"""
        for tr in tr_contents:
            if counter == 502:
                print("Se llegó a 500 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                continue
            time.sleep(0.5)
            if DarClick(browser, '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/form[1]/table/tbody/tr[' + str(counter) + ']/td[12]/a[4]') == False:
                print("Error al dar descargar archivo")
                continue
            counter += 1
            #/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/form[1]/table/tbody/tr[2]/td[12]/a[4]
            #/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/form[1]/table/tbody/tr[3]/td[12]/a[4]
"""