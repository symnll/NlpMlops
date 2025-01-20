import os
from pathlib import Path
import logging

#Loggin ayarlarının yapılması: Bilgileri zaman içinde yaptığımız işlemleri loglar yani bize bu işlemi şu zaman yaptın gibi veyahutta bu işlem şu zaman da yapıldı
logging.basicConfig(level = logging.INFO, format='[%(asctime)s]: %(message)s:')

#Projemizin bir ismi var ve isim üzerinden dosyalarımı oluşturmam gerekiyor.
project_name = "textSummarizer"

#Projemiz için geçerli olacak çalışma klasörlerini oluşturmaya başlayalım

list_of_files = [
    ".github/workflows/.gitkeep", #github için çalışma dosyası oluşturuyoruz. (Git ignore).
    f"src/{project_name}/__init__.py", #Projenin çalışma modülünün Python modülü gibi kullanmamızı sağlar.
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",#Projeyi yapılandırmak için kullanılır.
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",#yapılandırma dosyalarını düzenlemek için sıkça tercih ettiğimiz format
    "params.yaml",#Dışarıdan verdiğimiz parametreler ve methodları kullanmak için tercih ediyoruz.
    "app.py",
    "main.py",#Preojenin çalışmasında ana bir çalışma ortamı sunar
    "Dockerfile",
    "requirements.txt",#PRojemiz için gerekli olan kütüphane paketlerini içerisinde bulunduruyoruz.
    "setup.py",
    "research/trials.jpynb",

]

#Dosya ve dizinlerin oluşturulma kısmına geldik

for filepath in list_of_files:
    filepath = Path(filepath)#Dosya yolunu path objesine çevirmiş oldum
    filedir, filename = os.path.split(filepath)#Dosya yolu ve dosya adı olarak ayırmış oluyoruz.

    #Eğer dizinimiz mevcut değil ise bu dizini oluştur diyoruz.
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Oluşturulmuş dosya: {filedir} ve Dosyanın ismi {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Oluşturulan dosya: {filepath}")
    
    else:
        logging.info(f"{filename} Bu dosya zaten mevcut")
