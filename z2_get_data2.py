# coding=utf8
# https://documents.bvl.com.pe/neg_rv_alfa.html

from selenium import webdriver
from io import BytesIO
from selenium.common.exceptions import NoSuchElementException
import sys
import csv
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import os.path, time
import os
import csv
from os import remove
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import math

from bs4 import BeautifulSoup
import json
import csv
import io
import codecs
import sys
from getpass import getpass
#from mysql.connector import connect, Error
from getpass import getpass
#import mysql.connector

dia = 30

mes = 7
num_paginacion = 1

def BuscarComponente(browser, path):
	b = True
	cont = 0
	while b == True:
		try:
			componente = browser.find_element("xpath", path)
			encontrado = componente.text
			b = False
		except:
			time.sleep(1)
			cont += 1
			if cont > 120:
				print("No se encontró el componente --Buscar Componente-- " + str(path))
				print("Iteración N#" + str(cont))
				return False
	return True

def DarClick(browser, path):
	b = True
	cont = 0
	while b == True:
		try:
			if BuscarComponente(browser, path) == True:
				componente =  browser.find_element("xpath", path)
				componente.click()
				b = False
			else:
				b = True
		except:
			time.sleep(1)
			cont += 1
			if cont > 10:
				print("No se encontró el componente --Dar Click-- " + str(path))
				print("Iteración N#" + str(cont))
				return False
	return True

def DarClick_v2(browser, path):

	try:
		componente =  browser.find_element("xpath", path)
		componente.click()
		return True
	except:
		print("No se encontró el componente --Dar Click-- " + str(path))
		return False

#reload(sys)
#sys.setdefaultencoding("utf-8")
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout)


dia_str = "{:02d}".format(dia)
mes_str = "{:02d}".format(mes)

path_fecha = "/Users/lucaswongmang/Downloads/" + mes_str + "_" + dia_str

if not os.path.isdir(path_fecha):
	os.mkdir(path_fecha)

PATH_CHROME_DRIVER = "/Users/lucaswongmang/Downloads/chromedriver"
chromeOptions = webdriver.ChromeOptions()
path_fecha = "/Users/lucaswongmang/Downloads/" + str(mes_str) + "_" + str(dia_str)

prefs = {"download.default_directory" : path_fecha}
#chromeOptions.add_experimental_option("prefs",prefs)

browser = webdriver.Chrome(executable_path=PATH_CHROME_DRIVER,chrome_options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())

while True:

	k = (num_paginacion - 1) * 25

	pagina_inicio = "http://ecomprobantes.net.pe/dbnWeb/dbnWeb/dbnLogin.aspx"
	browser.get(pagina_inicio)
						   
	elem_user = browser.find_element("xpath", '/html/body/form/input[1]')

	elem_user.send_keys("EDWARD")
							
	elem_password = browser.find_element("xpath", '/html/body/form/input[2]')
	elem_password.send_keys("29535019")

	x = input("RAW Fin del Captcha")

	pagina_listado = "http://ecomprobantes.net.pe/dbnWeb/factura/facLisMonitorPeruPaginado.aspx?par1=DTE"
	browser.get(pagina_listado)

	time.sleep(1)

	elem_fecha_inicio = browser.find_element("xpath", '/html/body/form/table[2]/tbody/tr[1]/td/div/table/tbody/tr[1]/td[2]/input')
	browser.execute_script("arguments[0].setAttribute('value','2022-" + mes_str + "-" + dia_str + "')", elem_fecha_inicio)

	
	elem_fecha_fin = browser.find_element("xpath", '/html/body/form/table[2]/tbody/tr[1]/td/div/table/tbody/tr[2]/td[2]/input')
	browser.execute_script("arguments[0].setAttribute('value','2022-" + mes_str + "-" + dia_str + "')", elem_fecha_fin)


	elem_tipo = Select(browser.find_element("xpath", '/html/body/form/table[2]/tbody/tr[1]/td/div/table/tbody/tr[1]/td[6]/select'))
	elem_tipo.select_by_value('1')

	tam_paginador = int(25)

	elem_paginador = Select(browser.find_element("xpath", '/html/body/form/div[3]/table/tbody/tr[4]/td/table/tbody/tr/td[18]/select'))
	elem_paginador.select_by_value(str(tam_paginador))


	elem_buscar = browser.find_element("xpath", '/html/body/form/table[2]/tbody/tr[1]/td/div/table/tbody/tr[3]/td[4]/input')
	elem_buscar.click()

	x = input("RAW previo a la paginacion")

	for pag in range(1, num_paginacion, 1):

		elem_sig = browser.find_element("xpath", '/html/body/form/div[3]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/input')
		elem_sig.click()
		time.sleep(2)

	time.sleep(2)

	#x = input("despues")


	elem_total = browser.find_element("xpath", '/html/body/form/div[3]/table/tbody/tr[4]/td/table/tbody/tr/td[14]/span')
	tam_total = float(elem_total.text)

	num_paginas = int(math.ceil(tam_total/tam_paginador))

	print(tam_total, num_paginas) 

	flag_salida = False
	flag_error = False
	for pag in range(1, num_paginas + 1, 1):
		for i in range(2, int(tam_paginador)+2, 1):
			print("prev", i)
			k += 1
			if DarClick_v2(browser,'/html/body/form/table[2]/tbody/tr[2]/td/div/div[1]/table/tbody/tr[' + str(i) + ']/td[7]/a') == False:
				#if DarClick(browser, "/html/body/form/table[2]/tbody/tr[2]/td/div/div[1]/table/tbody/tr[2]/td[7]/a") == False:
				if k == int(tam_total):
					print("Termino la descarga del archivo")
					flag_salida = True
					break

				print("Error al descargar archivo")
				flag_error = True
				break

			print("for ", i, k, tam_total, num_paginacion + pag - 1)
			time.sleep(1)

		if flag_error:
			num_paginacion = num_paginacion + pag - 1
			print("break por flag_error")
			break

		if flag_salida:
			print("break por flag_salida")
			break

		print("salió del primer for")

		elem_sig = browser.find_element("xpath", '/html/body/form/div[3]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/input')
		elem_sig.click()
		time.sleep(4)

	print("salió del segundo for")
	#num_paginacion = num_paginacion + pag - 1

