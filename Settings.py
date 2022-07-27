# *****************************************************************************************
# библиотека для работы с форматом файла json, 
# данные хранятся в виде словаря (ключ = значение)
import json
# *****************************************************************************************
# Работа с директориями и файлами ОС
from merlib.fs.File import File
file = File()
# определить верную директорию файла настроек
file_settings = file.file_init_name('', './json/settings.json', __file__)
# определить верную директорию файла истории
file_history = file.file_init_name('', './json/history.json', __file__)
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
    # загрузка истории файла json
    def load_history(self, file_history: str=file_history) -> list:
        # считываем из файла
        with open(file_history, 'r') as file:
            return json.load(file)
    # ---------------------------------------------------------------------------
    # сохранение настроек файла json
    def save_settings(self, settings: dict, file_settings: str=file_settings) -> None:
        # записываем в файл данные в формате json
        with open(file_settings, 'w') as file:
            json.dump(settings, file, indent=4, sort_keys=True)
    # ---------------------------------------------------------------------------
    # сохранение истории файла json
    def save_history(self, history: list, file_history: str=file_history) -> None:
        # записываем в файл данные в формате json
        with open(file_history, 'w') as file:
            json.dump(history, file, indent=4, sort_keys=True)
    # ---------------------------------------------------------------------------
    # обновление настроек файла json
    def update_settings(self, **settings: dict) -> None:
        # записываем в файл данные в формате json
        with open(file_settings, 'w') as file:
            json.dump(settings, file, indent=4, sort_keys=True)
    # ---------------------------------------------------------------------------
    # обновление истории файла json
    def update_history(self, *history: list) -> None:
        # записываем в файл данные в формате json
        with open(file_history, 'w') as file:
            json.dump(history, file, indent=4, sort_keys=True)
    # ---------------------------------------------------------------------------
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

    print('-------------------------------------')
    print('+++++update_settings+++++')
    print(settings.load_settings())
    print(settings.update_settings(round='3', hist='777', vibro='0.1'))
    print(settings.load_settings())

    print('-------------------------------------')
    print('+++++load_history+++++')

    print(settings.load_history())

    print('-------------------------------------')
    print('+++++save_history+++++')

    arr = settings.load_history()
    arr.extend(['1', '2', '3'])
    settings.save_history(arr)
    print(settings.load_history())

    print('-------------------------------------')
    print('+++++update_history+++++')
    settings.update_history('1', '898', '3')
    print(settings.load_history())
# *****************************************************************************************