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
FULLXPATH_LISTAREPARTO = '/html/body/div[2]/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/ol'

Names = ['Robert Downey Jr.','Chris Hemsworth','Josh Brolin', 'Juan Antonio Bernal', 'Idzi Dutkiewicz',
         'Steve Rogers','Captain America','Chris Evans','Raúl Llorens','José Antonio Macías','Thanos',
         'Josh Brolin','José García Insúa','Juan Carlos Tinoco','Thor','Chris Hemsworth','Iván Labanda',
         'Scarlett Johansson','Don Cheadle','Benedict Cumberbatch','Tom Holland','Chadwick Boseman',
         'Zoe Saldana','Karen Gillan','Tom Hiddleston','Paul Bettany','Elizabeth Olsen','Anthony Mackie',
         'Sebastian Stan']

if __name__ == '__main__':

    serv = Service(PATH_TO_DRIVER)
    edgeBrowser = webdriver.Edge(service=serv)
    edgeBrowser.maximize_window()

    for i in range(0, len(Names)):
        try:
            edgeBrowser.get('https://www.bing.com/search?q=' + Names[i])
            edgeBrowser.implicitly_wait(5)
        except:
            pass
