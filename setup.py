import setuptools

#Readme.md dosyasını uzun açıklamayı alır
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

#Versiyon Numarası
__version__ = "0.0.0"

#Proje ve yazar bilgileri
REPO_NAME = "NlpMlops"
AUTHOR_USER_NAME = "symnll"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "notlarimd6@gmail.com"

#setuptools.setup kullanarak proje bilgilerini ayarlıyoruz.
setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description="Metni özetleyen Çalışma projesi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    procect_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",   
    },
    package_dir={"":"src"},#Paketin bulduğunu dizinin belirtiyoruz
    packages=setuptools.find_packages(where="src")#src dizinindeki tüm paketleri bulacak ve dahil edecek
)