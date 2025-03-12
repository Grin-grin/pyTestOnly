import logging
from datetime import datetime
import os

def setting_log(fileName):
    """Настройки логов"""

    # Создаем папку для логов, если её нет
    logFolder = "logs"
    if not os.path.exists(logFolder):
        os.makedirs(logFolder)

    currentDate = datetime.now().strftime("%d.%m.%Y_%H-%M-%S")
    logFile = os.path.join(logFolder, f"{currentDate}_log_{fileName}.log")

    # Настройки
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s: %(message)s", #Формат логов
        datefmt="%d.%m.%Y %H:%M:%S", #Формат времени
        handlers=[
            logging.FileHandler(logFile, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )