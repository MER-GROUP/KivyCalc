# *****************************************************************************************
# Работа с директориями и файлами ОС
from merlib.fs.File import File
file = File()
# определить верную директорию файла настроек
file_settings = file.file_init_name('', './setting.json', __file__)
# *****************************************************************************************
# Parse - разбор текстовых строк
class Settings:
    pass
# *****************************************************************************************