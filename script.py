import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

    # GLOBAL PATHS
PATH_TO_DRIVER = r'C:\Users\lucho\Documents\GitHub\microsoft-rewards-claimer-script\msedgedriver.exe'
#PATH_TO_BROWSER = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

FULLXPATH_LISTAREPARTO = '/html/body/div[2]/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/ol'

# FULLXPATH ITEMS LISTA
#                           /html/body/div[1]/main/div[2]/div/div[2]/div/div/div/div[2]/div/ol/li[1]
#                           /html/body/div[1]/main/div[2]/div/div[2]/div/div/div/div[2]/div/ol/li[2]


# FULLXPATH ITEMS LISTA 2

if __name__ == '__main__':

    serv = Service(PATH_TO_DRIVER)
    edgeBrowser = webdriver.Edge(service=serv)
    edgeBrowser.maximize_window()
    edgeBrowser.get('https://www.bing.com/search?q=avengers%3a+endgame+reparto&filters=dtbk:%22MCFvdmVydmlldyFzYXR2Ml9jYXN0X2VzITUyOWJlMjIxLTA5NzItNTdjNC0xMDBlLTA0MGE5Y2RiYjA2Nw%3d%3d%22+fcid:%22f34866e0-993d-ca64-05e6-190cf36d8def%22+sid:%22529be221-0972-57c4-100e-040a9cdbb067%22&FORM=DEPNAV')

    edgeBrowser.implicitly_wait(3)

    for i in range(1, 51):
        try:
            ITEMLISTA = edgeBrowser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/div/div[2]/div/ol/li[' + str(i) + ']/div/a')
#                                                           /html/body/div[1]/main/div[2]/div/div[2]/div/div/div/div[2]/div/ol/li[1]
#                                                           /html/body/div[1]/main/div[2]/div/div[2]/div/div/div/div[2]/div/ol/li[1]/div
#                                                           /html/body/div[1]/main/div[2]/div/div[2]/div/div/div/div[2]/div/ol/li[1]/div/a
#           ITEMLISTA.send_keys(Keys.COMMAND + 't')
            SEARCHNAME = ITEMLISTA.accessible_name
            print(SEARCHNAME)
            

#             ITEMLISTA.send_keys(Keys.CONTROL + 't')
        except:
            print('No encontró item / No pudo mandar keys')

    time.sleep(5)



