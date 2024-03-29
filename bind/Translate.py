# *****************************************************************************************
# Translate - автоматическая локализация программы на родной язык
class Translate:
    # ---------------------------------------------------------------------------
    # словарь руского и английского языка
    translate = {
        'about': [
            '[b][color=#C0C0C0]РАЗРАБОТЧИК И АВТОР:[/color][/b]\n' +
                    '[color=#808080]Максим Романенко (Red Alert)[/color]\n' +
                '[b][color=#C0C0C0]ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ:[/color][/b]\n' +
                    '[color=#808080]свободное и распространяется\n' +
                    'по лицензии MIT[/color]\n' +
                '[b][color=#C0C0C0]ИНСТРУМЕНТЫ РАЗРАБОТКИ:[/color][/b]\n' +
                    '[color=#808080]python (python.org), kivy (kivy.org),\n' +
                    'json (json.org), debian (debian.org),\n' +
                    'vscode (code.visualstudio.com),\n' +
                    'git (git-scm.com)[/color]\n' +
                '[b][color=#C0C0C0]КОД ПРОГРАММЫ:[/color][/b]\n' +
                    '[color=#808080]github.com/mer-group/kivycalc[/color]\n' +
                '[b][color=#C0C0C0]КОНТАКТЫ:[/color][/b]\n' +
                    '[color=#808080]i@mer-group.ru\n' +
                    'github.com/mer-group[/color]',

            '[b][color=#C0C0C0]DEVELOPER AND AUTHOR:[/color][/b]\n' +
                    '[color=#808080]Maxim Ramanenka (Red Alert)[/color]\n' +
                '[b][color=#C0C0C0]SOFTWARE:[/color][/b]\n' +
                    '[color=#808080]free and distributed\n' +
                    'under the MIT license[/color]\n' +
                '[b][color=#C0C0C0]DEVELOPMENT TOOLS:[/color][/b]\n' +
                    '[color=#808080]python (python.org), kivy (kivy.org),\n' +
                    'json (json.org), debian (debian.org),\n' +
                    'vscode (code.visualstudio.com),\n' +
                    'git (git-scm.com)[/color]\n' +
                '[b][color=#C0C0C0]PROGRAM CODE:[/color][/b]\n' +
                    '[color=#808080]github.com/mer-group/kivycalc[/color]\n' +
                '[b][color=#C0C0C0]CONTACTS:[/color][/b]\n' +
                    '[color=#808080]i@mer-group.ru\n' +
                    'github.com/mer-group[/color]'
        ],
        'info': [
            'ИНФО',
            'INFO'
        ],
        'close': [
            'ЗАКРЫТЬ',
            'CLOSE'
        ],
        'history': [
            'ИСТОРИЯ',
            'HISTORY'
        ],
        'clear': [
            'ОЧИСТИТЬ ИСТОРИЮ',
            'CLEAR HISTORY'
        ],
        'vibro': [
            'ВИБРАЦИОННЫЙ ОТКЛИК',
            'VIBRATION RESPONSE'
        ],
        'length': [
            'ДЛИНА ИСТОРИИ',
            'HISTORY LENGTH'
        ],
        'round': [
            'ОКРУГЛЕНИЕ ЧИСЕЛ',
            'ROUNDING NUMBERS'
        ],
        'settings': [
            'НАСТРОЙКИ',
            'SETTINGS'
        ]
    }
    # ---------------------------------------------------------------------------
    # переводит строку в английский или русский язык
    def get_translate(self, lang: str, name: str) -> str:
        try:
            if (lang.lower() in 'russianрусский'):
                return self.translate[name][0]
            else:
                return self.translate[name][1]
        except (KeyError):
            return 'KeyError'
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    print('-------------------------------------')
    print('+++++get_translate+++++')
    print(Translate().get_translate('en', 'info'))
    print(Translate().get_translate('en', 'error'))
# *****************************************************************************************