import os
import shutil

source = input("Enter name of the source folder : ")

destination = input("Enter name of the destination folder : ")

source = source + '/'

destination = destination + '/'

list_of_files = os.listdir(source)

for file in list_of_files : 
    shutil.copy((source + file), destination)