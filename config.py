import os

# Получаем абсолютный путь до текущей директории
ROOT_DIR = os.path.dirname(__file__)

# Создаем путь до директории data
DATA_DIR = os.path.join(ROOT_DIR, "html")

#Создаем путь до файла contacts.html относительно текущей директории.
REL_HTML_DIR = os.path.join(DATA_DIR, "../html/contacts.html")
CONTACTS = os.path.abspath(REL_HTML_DIR)
