# Peru_files
Download a database of donations from https://www.datosabiertos.gob.pe/, then send it to the workspace and unzip it, save the file in a directory, remove de zip file and finally with the info inside the csv file create new csv files with the regions name that contains the info of each region

1. First go into to the directory where you are going to save the proyect using the terminal
2. Clone the repository using the command "git clone https://github.com/Jescob47/Peru_files.git"
3. Go into the directory "Peru_files" and install the requirements using the command "pip install -r requirements.txt"
4. Change the values of "work_directory" and "download_directory", in the program Create_csv_files:

![image](https://user-images.githubusercontent.com/71473111/156906044-a2cbe700-aaa2-4213-b548-5af01c87e646.png)

5. Change the value of "file_downloaded" to the url where the file that was downloaded from the website is placed and add at the end "/pcm_donaciones.zip". In my case is 'D:/pcm_donaciones.zip', like in the image below. This must be done in the program Get_info_web:

![image](https://user-images.githubusercontent.com/71473111/156906097-c6cd81a2-9114-4707-a7e7-8d76c496fd1c.png)

6. Finaly run the program using the command "py Create_csv_files.py". It will create the directory "Csv_files" in the workspace.

![image](https://user-images.githubusercontent.com/71473111/156906004-15e1a789-2e62-4130-a438-e7b565a7e214.png)
