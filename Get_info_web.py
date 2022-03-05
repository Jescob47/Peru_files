import unittest
import time
import os

from mimetypes import init
from select import select
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""This program download a file from the main_url, with filter parameters like type, 
categorie, format to find a report with name report_name and donwload it
"""

main_url = 'https://www.datosabiertos.gob.pe/' # URL principal
chromedriver = './chromedriver'

type_table = '//*[@id="main"]/div/section/div/div/div/div/div[1]/div/div/h2'
type_content = 'facetapi-link--199'

categorie_table = '//*[@id="main"]/div/section/div/div/div/div/div[1]/div/div[2]/h2'
categorie = 'facetapi-link'

format_table = '//*[@id="main"]/div/section/div/div/div/div/div[1]/div/div[4]'
format_doc = 'facetapi-link--9'

word_to_search = 'donaciones'
report_name = 'Donaciones COVID-19 - [Ministerio de Economía y Finanzas - MEF]'


class FileToDownload(unittest.TestCase):
    """This class use functions to work with the webpage and download the file"""

    def __init__(self, chromedriver:str = chromedriver):
        """Initialize the variables"""
        self.web_page = webdriver.Chrome(chromedriver)

    def open_url(self):
        """This funtion opens the website and maximize the window"""
        self.web_page.get(main_url)
        self.web_page.maximize_window()

    def select_item(self, choice:str, table:str):
        """This funtion selects the parameter in the dropdown menu with name table, but
        before it verify if the parameter is enable and displayed, if not it opens 
        the dropdown menu and verify again if the parameter is enable and displayed to be choiced
        """
        var_choice = self.web_page.find_element_by_id(choice)
        if not var_choice.is_displayed():
            self.web_page.find_element_by_xpath(table).click()
            time.sleep(0.5)
        self.assertTrue(var_choice.is_displayed(),var_choice.is_enabled())
        var_choice.click()

    def set_parameters(self):
        """This funtion set the parameters, insert the document name, finds it and downloads it"""
        self.select_item(type_content, type_table)
        self.select_item(categorie, categorie_table)
        self.select_item(format_doc, format_table)
        name_to_search = self.web_page.find_element_by_name('query')
        name_to_search.send_keys(word_to_search)
        self.web_page.find_element_by_id('edit-submit-dkan-datasets').click()
        time.sleep(0.5)
        document = self.web_page.find_element_by_xpath('//*[@id="main"]/div/section/div/div/div/div/div[2]/div/div/div/div/div[3]/div/article/div[2]/h2/a')
        self.assertTrue(document.is_displayed, document.is_enabled())
        document.click()
        time.sleep(0.5)      
        download_botton = self.web_page.find_element_by_xpath('//*[@id="data-and-resources"]/div/div/ul/li[3]/div/span/a')
        self.assertTrue(download_botton.is_displayed(), download_botton.is_enabled())
        download_botton.click()

    def close_window(self):
        """This funtion closes the windows"""
        while not os.path.isfile('D:/pcm_donaciones.zip'):
            pass
        self.web_page.close()


"""if __name__=='__main__':
    run =FileToDownload(chromedriver)
    run.open_url()
    run.set_parameters()
    run.close_window()
"""