# *****************************************************************************************
# Translate - автоматическая локализация программы на родной язык
class Translate:
    # ---------------------------------------------------------------------------
    # словарь руского и английского языка
    translate = {
        'info': [
            'РАЗРАБОТЧИК И АВТОР:\n/\
                    Максим Романенко (Red Alert)\n/\
                ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ:\n/\
                    свободное и распространяется\n/\
                    по лицензии MIT\n/\
                ИНСТРУМЕНТЫ РАЗРАБОТКИ:\n/\
                    python (python.org), kivy (kivy.org),\n/\
                    json (json.org), debian (debian.org),\n/\
                    vscode (code.visualstudio.com),\n/\
                    git (git-scm.com)\n/\
                ИСХОДНЫЙ КОД ПРОГРАММЫ:\n/\
                    github.com/mer-group/kivycalc\n/\
                КОНТАКТЫ:\n/\
                    i@mer-group.ru\n/\
                    github.com/mer-group',

            'DEVELOPER AND AUTHOR:\n/\
                    Maxim Ramanenka (Red Alert)\n/\
                SOFTWARE:\n/\
                    free and distributed\n/\
                    under the MIT license\n/\
                DEVELOPMENT TOOLS:\n/\
                    python (python.org), kivy (kivy.org),\n/\
                    json (json.org), debian (debian.org),\n/\
                    vscode (code.visualstudio.com),\n/\
                    git (git-scm.com)\n/\
                THE SOURCE CODE OF THE PROGRAM:\n/\
                    github.com/mer-group/kivycalc\n/\
                CONTACTS:\n/\
                    i@mer-group.ru\n/\
                    github.com/mer-group'
        ]
    }
    # ---------------------------------------------------------------------------
    # переводит строку в английский или русский язык
    def get_translate(self, lang: str, name: str) -> str:
        if (lang.lower() in 'russianрусский'):
            return self.translate[name][0]
        else:
            return self.translate[name][1]
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    pass
# *****************************************************************************************