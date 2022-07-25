# *****************************************************************************************
# библиотека для работы с форматом файла json, 
# данные хранятся в виде словаря (ключ = значение)
import json
# *****************************************************************************************
# Работа с директориями и файлами ОС
from merlib.fs.File import File
file = File()
# определить верную директорию файла настроек
file_settings = file.file_init_name('', './settings.json', __file__)
# *****************************************************************************************
# Settings - настройки программы через json
class Settings:
    # ---------------------------------------------------------------------------
    # загрузка настроек файла json
    def load_settings(self, file_settings: str=file_settings) -> dict:
        # считываем из файла
        with open(file_settings, 'r') as file:
            return json.load(file)
    # ---------------------------------------------------------------------------
    # сохранение настроек файла json
    def save_settings(self, settings: dict, file_settings: str=file_settings) -> None:
        # записываем в файл данные в формате json
        with open(file_settings, 'w') as file:
            json.dump(settings, file, indent=4, sort_keys=True)
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    settings = Settings()

    print('-------------------------------------')
    print('+++++load_setting+++++')
    print(settings.load_settings())

    print('-------------------------------------')
    print('+++++save_settings+++++')
    my_settings = settings.load_settings()
    print(my_settings)
    my_settings['vibro'] = '0.4'
    settings.save_settings(my_settings)
    print('settings is save')
    my_settings = settings.load_settings()
    print(my_settings)
# *****************************************************************************************