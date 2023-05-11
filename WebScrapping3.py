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
        PATH_CHROME_DRIVER = "/Users/lucaswongmang/Downloads/chromedriver"
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

    browser.get('https://sfe.bizlinks.com.pe/sfeperu/login.jsf')


    if Escribir(browser, '/html/body/div[1]/div/div/div/div[6]/div[2]/form/table/tbody/tr[3]/td[2]/input', 'rsalazar@topsa.com.pe') == False:
        print("Error al escribir usuario")
        return

    if Escribir(browser, '/html/body/div[1]/div/div/div/div[6]/div[2]/form/table/tbody/tr[5]/td[2]/input[1]','Psicologia23') == False:
        print("Error al escribir clave")
        return

    if DarClick(browser, '/html/body/div[1]/div/div/div/div[6]/div[2]/form/table/tbody/tr[9]/td[2]/button') == False:
        print("Error al dar click en buscar")
        return

    if DarClick(browser, '/html/body/div[2]/div[2]/form/div/div/div[2]/div[1]/div/ul/li[1]/a') == False:
        print("Error al dar click en cuadritos")
        return
################### SACAR DATOS ###################
    if DarClick(browser, '/html/body/div[3]/div/form[1]/div/div[2]/button[1]') == False:
        print("Error al dar click en buscar")
        return
    #/html/body/div[3]/div/form[1]/div/div[2]/button[1]
    #/html/body/div[3]/div/form[2]/div[2]/div[2]/div/div[1]/div/table/thead/tr/th[1]/div/div/div/span
    time.sleep(5)
    array = []
    temparray=[]
    cont = 0
    pag = Select(browser.find_element_by_xpath("/html/body/div[3]/div/form[2]/div[2]/div[2]/div/div[3]/div/table/tfoot/tr/td/select"))
    pag.select_by_index(3)

    a = True
    counter = 1
    contPagina=2
    row = ""
    contador = 2
    cacPagina=7
    txt = browser.find_element_by_xpath("/html/body/div[3]/div/form[2]/div[2]/div[2]/div/div[3]/div/table/tfoot/tr/td/span[1]").text
    txt2=txt.replace(")", "")
    print(txt2)
    arr = txt2.split(" ")
    num = int(arr[2])
    print(num)

    while a==True:
        #time.sleep(1)
        elem_tabla = BuscarObjeto(browser, '/html/body/div[3]/div/form[2]/div[2]/div[2]/div/div[2]/table/tbody')
        #tr_contents2 = elem_tabla.find_element_by_tag_name('tbody')

        tr_contents = elem_tabla.find_elements_by_tag_name('tr')
        ##############
        time.sleep(2)
        if DarClick(browser,'/html/body/div[3]/div/form[2]/div[2]/div[2]/div/div[1]/div/table/thead/tr/th[1]/div/div/div') == False:
            print("Error al dar click en buscar facturas por rango")
            return
        if DarClick(browser,'/html/body/div[3]/div/form[2]/div[1]/div[2]/span[2]/button') == False:
            print("Error al dar click en buscar facturas por rango")
            return
        time.sleep(1)
        browser.find_element_by_id("descargarSeleccionadosXmlButton").click()
        ##############
        #/html/body/div[3]/div/form[2]/div[1]/div[2]/span[2]/button
        #if DarClick(browser,'/html/body/div[3]/div/form[2]/div[1]/div[2]/button') == False:
        #    print("Error al dar click en exportar_Lista")
        #    return
        time.sleep(1000)

        try:
            counter=1
            time.sleep(2)
            if contador==num-3:
                if DarClick(browser,'/html/body/div[3]/div/form[2]/div[2]/div[2]/div/div[3]/div/table/tfoot/tr/td/span[4]/span['+str(cacPagina)+']') == False:
                    print("Error al dar click en siguiente pagina")
                    return
                cacPagina += 1
                #/html/body/div[2]/div[3]/form/div[3]/div/div/table/tbody/tr/td[15]
                print(cacPagina)
            elif cacPagina<num-12 and contPagina > 6:
                contador = contador + 1
                if DarClick(browser,'/html/body/div[3]/div/form[2]/div[2]/div[2]/div/div[3]/div/table/tfoot/tr/td/span[4]/span['+str(cacPagina)+']') == False:
                    print("Error al dar click en siguiente pagina")
                    return
                #/html/body/div[2]/div[3]/form/div[3]/div/div/table/tbody/tr/td[15]
                print(cacPagina)
            else:
                contador = contador + 1
                if DarClick(browser,'/html/body/div[3]/div/form[2]/div[2]/div[2]/div/div[3]/div/table/tfoot/tr/td/span[4]/span['+str(contPagina)+']') == False:
                    print("Error al dar click en siguiente pagina")
                    return
                print(contPagina)
                contPagina += 1
        except:
            a=False
            print("No se encontró más páginas")


    print("Adios")
DescargarFacturas('01-01-2021', '05-01-2021')

