import os

print(os.getcwd()) # nerde çalıştığı
print(os.listdir()) # çalıştığı dizindeki dosyaları listeler
print(os.listdir('C:\\Users')) # Users dizindeki dosyaları listeler


import shutil

#shutil.move('practice.py','C:\\Users\\nuatli\\Documents\\asd')
print(os.listdir('C:\\Users\\nuatli\\Documents\\asd')) # Users dizindeki dosyaları listeler


'''
Deletin Files
    os.unlink(path)
    os.rmdir(path) 
    shutil.rmtree(path) -> tehlikeli
    
    bunun yerine send2tarsh da kullanılabilir.
'''

file_path='C:\\Users\\nuatli\\Documents\\asd\\python-learning-basic'
for folder,sub_folders,files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print('\n')
    print('This subfolders are : ')
    for sub_fold in sub_folders:
        print(f"\t Subfolder : {sub_fold}")
    print('\n')
    print('This files are : ')
    for f in files:
        print(f"\t File : {f}")
    print('\n')
        