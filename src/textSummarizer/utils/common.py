import os
from box.exceptions import BoxValueError #YAML dosyalarımızın boş olma durumunu kontrol etmek için veya yakalamak için
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations #Kodda tip kontrolü ve doğrulama yapmak için
from box import ConfigBox #Yaml içeriğini koruyoruz.
from pathlib import Path
from typing import Any#İp uçları sağlamak için typing içindeki ANY tipini tercih ederiz.


