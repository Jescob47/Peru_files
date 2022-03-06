import shutil
import pandas as pd
import os
import unittest

from os import remove
from Get_info_web import FileToDownload
from zipfile import ZipFile

"""This program use Get_info_web to download a zip file, then send it to the workspace 
and unzip it, save the file in a directory, remove de zip file and finally with the info 
inside the csv file create new csv files with the regions name that contains the info of each region
"""

download_directory = 'D:/'
file_name = 'pcm_donaciones.zip'
csv_directory = 'Csv_files'
work_directory = 'D:/OneDrive - Universidad EAFIT/U/proyectos julian/Programacion/Prueba pagina peru/'

class CreateCSVFiles(unittest.TestCase):
    def organize_download_zip(self):
        """This funtion moves the zip file from the download diretory to the workspace directory,
        extracts de zip file in a csv directory and removes the zip file
        """
        self.assertTrue(os.path.isfile(download_directory + file_name))
        shutil.move(download_directory + file_name, work_directory + file_name)
        with ZipFile(file_name, 'r') as zip:
            zip.extractall(csv_directory)
            print('File is unzipped in folder %s' %csv_directory)
        self.assertTrue(os.path.isdir(work_directory + csv_directory))
        remove(file_name)
        self.assertFalse(os.path.isfile(download_directory + file_name))
        print('Zip file removed')

    def create_new_csv_files(self):
        """This function reads the csv file, extract the regions and create files of each region with 
        the correspondent info
        """
        data = pd.read_csv('./'+ csv_directory + '/' + file_name[:-3] + 'csv', index_col=0, encoding='latin-1')
        regions = data['REGION'].unique()
        for i in range(len(regions)):
            new_csv = data[data['REGION']==regions[i]]
            self.assertTrue(os.path.isdir(work_directory + csv_directory))
            new_csv.to_csv('./' + csv_directory + '/' + regions[i].lower() + '.csv') 
        
    def main(self):
        """This funtcion is were the other functions are runed"""
        download_zip = FileToDownload()
        download_zip.open_url()
        download_zip.set_parameters()
        download_zip.close_window()
        try:
            self.organize_download_zip()
        except FileNotFoundError:
            print("The field %s does not exist" %file_name)
        else:
            self.create_new_csv_files()

if __name__=="__main__":
    run = CreateCSVFiles()
    run.main()