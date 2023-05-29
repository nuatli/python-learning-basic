'''
import shutil
shutil.unpack_archive('unzip_me.zip')
'''


import zipfile
import os
import shutil
import re

#print(os.listdir())

def get_zip_file_names():
    file_names = []
    for file_name  in os.listdir():
        if file_name.endswith(".zip"):
            file_names.append(file_name)
    return file_names
    
def get_folder_names():
    file_names = []
    path = os.getcwd()
    for file  in os.listdir():
        if os.path.isdir(file):
            file_names.append(file)
            print(file)
    return file_names
    
    
    
zip_files = get_zip_file_names()

for zip_file in zip_files:
    print(zip_file)
    

shutil.unpack_archive(zip_files[0])

print("######")


folder_names = get_folder_names()


with open(folder_names[0]+'/Instructions.txt') as f:
    content = f.read()
    print(content)
    
   

current_pattern = r'\d{3}-\d{3}-\d{4}'

test_string = 'here is a a phone number 123-123-1234'

re.findall(current_pattern,test_string)

def search(file,pattern=current_pattern):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return '' ## yada pass

results = []


print(os.getcwd()+folder_names[0])

for folder,subfolders,files in os.walk(os.getcwd()+'\\'+folder_names[0]):
    for f in files:
        #print(folder)
        #print(f)
        full_path = folder+'\\'+f
        results.append(search(full_path))
        
        
for r in results:
    if r != '':
        print(r.group())