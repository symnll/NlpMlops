import os 
import sys 
import logging

logging_str = "[%(asctime)s: %(levelname)s:%(module)s:%(message)s]"

#Log dosyasının kayıtlı olmasını istediğimiz dizin ve dosya adı

log_dir = "logs" #Logların kaydedileceği kısım
log_filepath = os.path.join(log_dir,"running_logs.log")#Tam olarak log dosyası yolu

os.makedirs(log_dir, exist_ok=True)#Dizin yok isine oluşturacak

#Yapılandırma kısmı
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[ # Logların nereye yönlendirileceğini belirliyoruz.
        logging.FileHandler(log_filepath), # Logları dosyaya yazdırır
        logging.StreamHandler(sys.stdout) # logları ekrana yazdırır
    ]
)

#Log nesnesinin oluşturulmnası
logger = logging.getLogger("textSummarizerLogger")

