import os
import shutil

# Write the name of directory here that needs to get sorted
path = input("Enter the name of the directory to be sorted : ")
# This will create a properly organised list with all the file name that is there in the directory
list_of_files = os.listdir(path)

for file in list_of_files :
    name , ext  = os.path.splitext(file)
    ext = ext[1:]
    if ext == "" : 
        continue
# This will move the file to the directory where the name 'ext' alrady exists
    if os.path.exists(path + '/' + ext) : 
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
# This will create a new directory if the diretory already doesn't exist
    else : 
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)