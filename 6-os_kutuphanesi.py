import os
print(os.name)
currentDir=os.getcwd() #bulunduğumuz klasör 
print(currentDir)

#new folder
folder_name="new_folder"
os.mkdir(folder_name)

#rename
new_folder_name="new_folder_2"
os.rename(folder_name,new_folder_name) #isim değişti

#yeni oluşturduğumuz klasörün içerisine girme
os.chdir(currentDir+"\\"+new_folder_name)
print(os.getcwd()) #klasörün içerisine girmiş olduk

#ilk bulunduğumuz klasöre döndük
os.chdir(currentDir)
print(os.getcwd())

files=os.listdir() #bulunduğumuz klasör içerisindeki dosyaları listeler
print(files)


#sonu ".py" ile biten dosyaları listeledik
for f in files:
    if f.endswith(".py"):
        print(f)
        

#oluşturduğumuz klasörü silme
os.rmdir(new_folder_name)

for i in os.walk(currentDir):
    print(i)
    

#aradığımız dosya var mı yok mu diye kontrol etme
os.path.exists("5-matplotlib_pyplot.py")