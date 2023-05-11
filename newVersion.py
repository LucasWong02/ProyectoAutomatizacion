from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


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


def GenerarBrowser():
    try:
        PATH_CHROME_DRIVER = r"C:\\Users\\jramirez110\\Documents\\ROBOT\\chromedriver.exe"
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("prefs", {
            "download.default_directory": "C:\\Users\\jramirez110\\Downloads\\FACTURAS",
        })
        return webdriver.Chrome(executable_path=PATH_CHROME_DRIVER, chrome_options=chromeOptions,
                                desired_capabilities=chromeOptions.to_capabilities())
    except:
        return False


def DescargarFacturas(fechaInicio, FechaFin):
    browser = GenerarBrowser()
    if browser == False:
        print("Error al generar navegador")
        return

    browser.get('http://asp402r.paperless.com.pe/Facturacion/login.jsp')

    if Escribir(browser, '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/input', '20337564373') == False:
        print("Error al escribir RUC")
        return

    if Escribir(browser, '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[3]/td[2]/input', 'mprado') == False:
        print("Error al escribir usuario")
        return

    if Escribir(browser, '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td[2]/input[1]',
                'Directivos#47') == False:
        print("Error al escribir clave")
        return

    if DarClick(browser, '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[5]/td/input') == False:
        print("Error al dar click en buscar")
        return

    if DarClick(browser,
                '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[3]/a') == False:
        print("Error al dar click en gestión documental")
        return

    if DarClick(browser,
                '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[1]/a') == False:
        print("Error al dar click en documentos emitidos")
        return

    if Escribir(browser,
                '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/div/form[1]/table/tbody/tr[3]/td[3]/table/tbody/tr[10]/td/input[1]',
                fechaInicio) == False:
        print("Error al escribir fecha inicio")
        return

    if Escribir(browser,
                '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/div/form[1]/table/tbody/tr[3]/td[3]/table/tbody/tr[10]/td/input[2]',
                FechaFin) == False:
        print("Error al escribir fecha inicio")
        return

    if DarClick(browser, '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/div/form[1]/input[2]') == False:
        print("Error al dar click en buscar facturas por rango")
        return

    if DarClick(browser,
                '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table[2]/tbody/tr/td[2]/a[5]') == False:
        print("Error al dar click en visualizar 500")
        return

    contPagina, a = 5, True

    while a == True:
        counter = 2
        elem_tabla = BuscarObjeto(browser, '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/form[1]/table')
        tr_contents = elem_tabla.find_elements_by_tag_name('tr')
        for tr in tr_contents:
            if counter == 502:
                print("Se llegó a 500 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                continue
            if DarClick(browser,
                        '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/form[1]/table/tbody/tr[' + str(
                                counter) + ']/td[14]/a[4]') == False:
                print("Error al dar click en xml")
                return
            print(counter)
            counter += 1
        contPagina += 1
        print("salió del for")
        try:
            print('/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table[2]/tbody/tr/td[2]/a[' + str(
                contPagina) + ']')
            if DarClick(browser,
                        '/html/body/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td[3]/table[2]/tbody/tr/td[2]/a[' + str(
                                contPagina) + ']') == False:
                print("Error al dar en cambiar a página: " + str(contPagina))
                a = False
                return
        except:
            a = False
            print("No se encontró más páginas")
    print("Culminé")

    if DarClick(browser, '/html/body/table[1]/tbody/tr[1]/td[4]/table/tbody/tr[1]/td/div/a') == False:
        print("Error al dar click en salir")
        return

    print("Se terminó de descargas las facturasxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


DescargarFacturas('01-01-2021', '05-01-2021')

