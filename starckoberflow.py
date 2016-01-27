# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os
os.system('clear')

urlBase = "http://stackoverflow.com/questions/tagged/java?"

print ""



maxPages = int(raw_input("Ingrese la pagina ala que desea acceder: "))
counter = 0

# Construyo la URL
url = "%spage=%d&sort=newest&pagesize=15" %(urlBase,maxPages)
print "     ##########################################"
print "  ------------------ PAGINA --- %d ---------------" %(maxPages)
print "        ##################################"

# Realizamos la petición a la web
req = requests.get(url)
# Comprobamos que la petición nos devuelve un Status Code = 200
statusCode = req.status_code
if statusCode == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text)

    # Obtenemos todos los divs donde estan las entradas
    entradas = html.find_all('div',{'class':'question-summary'})

    # Recorremos todas las entradas para extraer el título, autor y fecha            
    for entrada in entradas:
        counter += 1
        pregunta = entrada.find('a', {'class' : 'question-hyperlink'}).getText()
        respuesta = entrada.find('div', {'class' : 'excerpt'}).getText()
        usuario = entrada.find('div', {'class' : 'user-details'}).getText()

        print "-----------------------------------------"
        print "------------ COMENTARIO --- %d ----------" %(counter)
        print "-----------------------------------------\n\n"

        # Imprimo el Título, Autor y Fecha de las entradas
        print "'PREGUNTA:##' %s \n'RESPUESTA:##' %s \n" %(pregunta,respuesta)

        print " _________________________________________"
        print "              USUARIO # %s                " %(usuario)
        print " ***************************************** \n\n"

else:
    # Si ya no existe la página y me da un 400
    print "hoal"