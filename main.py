# *****************************************************************************************
# KivyCalc - простой калькулятор для простых и повседневных вычеслений
# *****************************************************************************************
# версия проекта
__version__ = '3.33'
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# свойства объекта (виджета)
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
# определение ОС
from kivy.utils import platform
# *****************************************************************************************
# глобальные переменные
# длина истории label_display_comment (коиличество вомволов)
# limit_history = 100
limit_history = 25
# является ли ОС - android
os_is_android = True
# *****************************************************************************************
# если не ОС не android, то применить следующие настройки
if not 'android' == platform:
    # конфигурация приложения kv
    from kivy.config import Config
    # задаем размеры окна статически
    Config.set('graphics', 'width', '300')
    Config.set('graphics', 'height', '300')
    # запрещаем изменение размеров окна
    Config.set('graphics','resizable', False)
    # длиина истории label_display_comment (коиличество вомволов)
    limit_history = 40
    # является ли ОС - android
    os_is_android = False
# *****************************************************************************************
# глобальная переменная
# разрешен ли доступ на чтение и запись файлов
is_access_open = True

# если ОС Android, то загрузить следующие модули
if 'android' == platform:
    # ----------------------------------------------------------------------
    # модуль plyer - работа с железом устройства
    # from plyer import vibrator
    # ----------------------------------------------------------------------
    # permissions - права доступа на чтение и запись файлов
    from android.permissions import Permission, request_permissions, check_permission

    # проверить права доступа
    def check_permissions(perms):
        for perm in perms:
            if check_permission(perm) != True:
                is_access_open = False
                return False
        return True

    # определить права доступа
    perms = [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE]
        
    # Получить права доступа на чтение и запись
    while check_permissions(perms)!= True:
        request_permissions(perms)
    # ----------------------------------------------------------------------
# *****************************************************************************************
# Работа с директориями и файлами ОС
# listdir - показывает файлы в конкретной папке
from os import listdir
# Работа с директориями и файлами ОС
from os.path import dirname, join
# Работа с директориями и файлами ОС
from pathlib import Path
# Класс Builder - закрузчик языка KV Lang
from kivy.lang import Builder
# Builder.load_file(str(Path(join(dirname(__file__), './design/'))))
# записываем директорию в переменную kv_path
folder = './design/'
kv_path = str(Path(join(dirname(__file__), folder)))
# загрузить все файлы .kv по отдельности
for file in listdir(kv_path):
    kv_path_file = str(Path(join(kv_path, file)))
    Builder.load_file(kv_path_file)
# *****************************************************************************************
# decimal - работа с десятичными числами
from decimal import Decimal
# *****************************************************************************************
# собственные модули
# Parse - разбор текстовых строк
from Parse import Parse
# Settings - настройки программы через json
from Settings import Settings
# Работа с директориями и файлами ОС
from merlib.fs.File import File
file = File()
# Design - манипуляции (действия) с объектами kivy
from bind.Design import Design
# Hardware - манипуляции (действия) с железом устройства
from bind.Hardware import Hardware
# *****************************************************************************************
# Действия программы
class Calc(BoxLayout):
    # ---------------------------------------------------------------------------
    '''root widget'''
    # ---------------------------------------------------------------------------
    # vars
    # ---------------------------------------------------------------------------
    label_display = ObjectProperty(None)
    label_display_comment = ObjectProperty(None)
    label_display_memory = ObjectProperty(None)
    display_clear = False
    push_back = False
    push_equal = False
    zero = False
    write_number = None
    temp_number = float()
    result_number = float()
    operand = None
    previous_operand = None
    calc_arr = list()
    # ---------------------------------------------------------------------------
    # methods
    # ---------------------------------------------------------------------------
    # нажатие цифровых кнопок и кнопки 'точка'
    # 1. если дисплей не очищен то очистить
    # (указывать в операндах self.display_clear = True)
    # 2. проверка числа на float
    # (проверки если были первыми введены знаки '-', '.', '0', '00', '01' и тд.)
    # 3. проверка числа на float через исключение
    # 4. записываем проверенное число на дисплей калькулятора
    # 5. записываем в переменную write_number итоговое введенное проверенное число
    # 6. записываем историю ввода чисел в переменную label_display_comment
    # 7. записываем в переменную previous_operand предыдущий операнд
    # 8. записываем в переменную operand текущий операнд
    # 9. определяем в переменную zero истину если итоговое число '0'
    # и ложь если итоговое число не '0'
    # 10. если кнопка equal была нажата то пометить что она не была нажата (push_equal = False)
    # далее очистить и записать в историю label_display_comment ответ результата вычесления
    def write_digit(self, button): 
        if self.display_clear and not self.push_back : # 1
            self.label_display.text = ''
            self.display_clear = False
        elif (self.push_equal):
            self.label_display.text = ''
            self.label_display_comment.text = ''
            self.push_equal = False

        digit_begin = button.text # 2
        if ('-' == digit_begin) and ('' == self.label_display.text):
            digit_begin = '-0'
        elif ((2 == len(self.label_display.text))
            and ('-0' == self.label_display.text)
            and ('0' == digit_begin)
            ):
            # test ##############################
            print('!!!!!!! RETURN 1 !!!!!!!') ###
            return
        elif ((2 == len(self.label_display.text))
            and ('-0' == self.label_display.text)
            and (chr(183) != digit_begin)
            ):
            digit_begin = '-' + digit_begin
            self.label_display.text = ''
        elif ((2 == len(self.label_display.text))
            and ('-0' == self.label_display.text)
            and (chr(183) == digit_begin)
            ):
            digit_begin = '-0.'
            self.label_display.text = digit_begin
        elif ((1 == len(self.label_display.text))
            and ('-' == self.label_display.text)
            and (chr(183) == digit_begin)
            ):
            digit_begin = '-0.'
            self.label_display.text = digit_begin
        elif ((1 == len(self.label_display.text))
            and ('0' == self.label_display.text)
            and (digit_begin in '123456789')
            ):
            pass
        elif ((('0' == digit_begin) or (chr(183) != digit_begin))
            and ('' != self.label_display.text)
            and (1 == len(self.label_display.text)) 
            and ('0' == self.label_display.text[0])
            ):
            # test ##############################
            print('!!!!!!! RETURN 2 !!!!!!!') ###
            return
        elif (chr(183) == digit_begin) and (0 == len(self.label_display.text)):
            digit_begin = '0.'
        elif (chr(183) == digit_begin):
            digit_begin = '.'

        if ('-0.' == digit_begin): # 3
            digit_end = self.label_display.text
        else:
            digit_end = self.label_display.text + digit_begin 
        try: 
            if float(digit_end):
                pass 
            else:
                pass          
        except (ValueError):
            # test ######################################################
            print('------------------------------------------------') ###
            print('!!!!!!!!!!!!!!!!!!! EXCEPTION !!!!!!!!!!!!!!!!!!') ###
            print(f'!!!!!!!!!!!!digit_end = {digit_end}!!!!!!!!!!!!') ###
            return

        if ('-0.' == digit_begin): # 4
            self.label_display.text = digit_begin
        elif ((digit_begin in '123456789') 
            and (1 == len(self.label_display.text))
            and ('0' == self.label_display.text)
            ):
            self.label_display.text = digit_begin
            digit_end = self.label_display.text
            self.label_display_comment.text = self.label_display_comment.text[: -1]
        else:
            self.label_display.text += digit_begin 
        self.write_number = digit_end # 5

        if (('' != self.label_display.text) # 6
            and (('-' == self.label_display.text[0]) 
                or ('0.' == self.label_display.text))
            and (2 == len(self.label_display.text))
            ):
            if (2 <= len(self.label_display_comment.text)):
                self.label_display_comment.text = Parse().back_to_operand(self.label_display_comment.text)
                self.label_display_comment.text += str(self.write_number)
            else:
                self.label_display_comment.text = str(self.write_number)
        elif (('' != self.label_display.text)
            and ('-0.' == self.label_display.text)
            and (3 == len(self.label_display.text))
            ):
            if (2 < len(self.label_display_comment.text)):
                self.label_display_comment.text = Parse().back_to_operand(self.label_display_comment.text)
                self.label_display_comment.text += str(self.write_number)
            else:
                self.label_display_comment.text = str(self.write_number)
        elif (('' != self.label_display.text)
            and ('-' == self.label_display.text[0])
            ):
            if (2 < len(self.label_display_comment.text)):
                self.label_display_comment.text = Parse().back_to_operand(self.label_display_comment.text)
                self.label_display_comment.text = self.label_display_comment.text[: -1]
                self.label_display_comment.text += str(self.write_number)
            else:
                self.label_display_comment.text = str(self.write_number)
        elif ((self.push_back) 
            and ('' != self.label_display.text)
            ):
            if (0 == len(self.calc_arr)):
                self.label_display_comment.text = str(self.write_number)
            else:
                self.label_display_comment.text = Parse().back_to_operand(self.label_display_comment.text)
                self.label_display_comment.text += str(self.write_number)
        else:
            # test ######################################################
            print('------------------------------------------------') ###
            print('!!!!!!!!!!!!!!!!!!!!!HISTORY!!!!!!!!!!!!!!!!!!!!') ###
            self.label_display_comment.text += str(self.write_number)[-1]
    
        self.previous_operand = self.operand # 7
        self.operand = 'w' # 8

        if (0 == float(self.label_display.text)): # 9
            self.zero = True
        else:
            self.zero = False

        if (self.push_equal): # 10
            self.push_equal = False
            self.label_display_comment.text = self.write_number

        # test ######################################################
        print('------------------------------------------------') ###
        print(' write write_number =', self.write_number) ###########
        print(' write temp_number =', self.temp_number) #############
        print(' write result_number =', self.result_number) #########
        print(' write operand =', self.operand) #####################
        print(' write previous_operand =', self.previous_operand) ###
        print(' write calc_arr =', self.calc_arr) ###################
        print(' write digit_end =', digit_end) ######################
        print(' write zero =', self.zero) ###########################
        print(' write push_back =', self.push_back) #################
        print(' write push_equal =', self.push_equal) ###############
    # ---------------------------------------------------------------------------
    # операнд сложения чисел
    # 1. условия проверки нажятия кнопки '+'
    # 2. пометить переменную display_clear в True
    # (при следующем вводе цифр очистить дисплей калькулятора)
    # 3. записываем в переменную previous_operand предыдущий операнд
    # 4. записываем в переменную operand текущий операнд
    # 5. записываем историю в label_display_comment
    # 6. записать в список (массив) итоговую переменную write_number и примененный operand
    # 7. пометить что кнопка back ('<') была не нажата
    # 8. если кнопка equal была нажата то пометить что она не была нажата (push_equal = False)
    # далее очистить и записать в историю label_display_comment ответ результата вычесления
    # и текущий операнд
    # 9. обрезать историю label_display_comment если она длинная
    def add(self):
        if ('=' == self.operand) and (self.previous_operand in 'w<'): # 1
            pass
        elif ((0 < len(self.calc_arr)) 
            and ('/' == self.calc_arr[-1])
            and ((self.write_number is None) or (0 == float(self.write_number)))
            ):
            return
        elif (('<' == self.operand)
            # and (self.previous_operand in 'w<-+*/%')
            and (self.previous_operand in 'w<-+*/%=')
            and (self.write_number is not None)
            ):
            if (self.label_display_comment.text[-1] in '-+*/%'):
                self.label_display_comment.text += self.label_display.text       
        elif ('=' == self.operand) and ('+' == self.previous_operand):
            return
        elif ('w' != self.operand):
            return

        self.display_clear = True # 2

        self.previous_operand = self.operand # 3
        self.operand = '+' # 4

        self.label_display_comment.text += str(self.operand) # 5

        self.calc_arr.append(self.write_number) # 6
        self.calc_arr.append(self.operand)

        self.push_back = False # 7

        if (self.push_equal): # 8
            self.push_equal = False
            self.label_display_comment.text = self.write_number
            self.label_display_comment.text += str(self.operand)

        # 9
        self.label_display_comment.text = Parse().history_trim(self.label_display_comment.text,
                                                                limit_history)

        # test ######################################################
        print('------------------------------------------------') ###
        print(' add write_number =', self.write_number) #############
        print(' add temp_number =', self.temp_number) ###############
        print(' add result_number =', self.result_number) ###########
        print(' add operand =', self.operand) #######################
        print(' add previous_operand =', self.previous_operand) #####
        print(' add calc_arr =', self.calc_arr) #####################
        print(' add zero =', self.zero) #############################
        print(' add push_back =', self.push_back) ###################
        print(' add push_equal =', self.push_equal) #################
    # ---------------------------------------------------------------------------
    # операнд вычитания чисел
    # 1. условия проверки нажятия кнопки '-'
    # 2. пометить переменную display_clear в True
    # (при следующем вводе цифр очистить дисплей калькулятора)
    # 3. записываем в переменную previous_operand предыдущий операнд
    # 4. записываем в переменную operand текущий операнд
    # 5. записываем историю в label_display_comment
    # 6. записать в список (массив) итоговую переменную write_number и примененный operand
    # 7. пометить что кнопка back ('<') была не нажата
    # 8. если кнопка equal была нажата то пометить что она не была нажата (push_equal = False)
    # далее очистить и записать в историю label_display_comment ответ результата вычесления
    # и текущий операнд
    # 9. обрезать историю label_display_comment если она длинная
    def subtract(self):
        if ('=' == self.operand) and (self.previous_operand in 'w<'): # 1
            pass
        elif ((0 < len(self.calc_arr)) 
            and ('/' == self.calc_arr[-1])
            and ((self.write_number is None) or (0 == float(self.write_number)))
            ):
            return
        elif (('<' == self.operand)
            # and (self.previous_operand in 'w<-+*/%')
            and (self.previous_operand in 'w<-+*/%=')
            and (self.write_number is not None)
            ):
            if (self.label_display_comment.text[-1] in '-+*/%'):
                self.label_display_comment.text += self.label_display.text
        elif ('=' == self.operand) and ('-' == self.previous_operand):
            return
        elif ('w' != self.operand):
            return

        self.display_clear = True # 2

        self.previous_operand = self.operand # 3
        self.operand = '-' # 4

        self.label_display_comment.text += str(self.operand) # 5

        self.calc_arr.append(self.write_number) # 6
        self.calc_arr.append(self.operand)

        self.push_back = False # 7

        if (self.push_equal): # 8
            self.push_equal = False
            self.label_display_comment.text = self.write_number
            self.label_display_comment.text += str(self.operand)

        # 9
        self.label_display_comment.text = Parse().history_trim(self.label_display_comment.text,
                                                                limit_history)

        # test #########################################################
        print('------------------------------------------------') ######
        print(' subtract write_number =', self.write_number) ###########
        print(' subtract temp_number =', self.temp_number) #############
        print(' subtract result_number =', self.result_number) #########
        print(' subtract operand =', self.operand) #####################
        print(' subtract previous_operand =', self.previous_operand) ###
        print(' subtract calc_arr =', self.calc_arr) ###################
        print(' subtract zero =', self.zero) ###########################
        print(' subtract push_back =', self.push_back) #################
        print(' subtract push_equal =', self.push_equal) ###############
    # ---------------------------------------------------------------------------
    # операнд умножения чисел
    # 1. условия проверки нажятия кнопки '*'
    # 2. пометить переменную display_clear в True
    # (при следующем вводе цифр очистить дисплей калькулятора)
    # 3. записываем в переменную previous_operand предыдущий операнд
    # 4. записываем в переменную operand текущий операнд
    # 5. записываем историю в label_display_comment
    # 6. записать в список (массив) итоговую переменную write_number и примененный operand
    # 7. пометить что кнопка back ('<') была не нажата
    # 8. если кнопка equal была нажата то пометить что она не была нажата (push_equal = False)
    # далее очистить и записать в историю label_display_comment ответ результата вычесления
    # и текущий операнд
    # 9. обрезать историю label_display_comment если она длинная
    def multiply(self):
        if ('=' == self.operand) and (self.previous_operand in 'w<'): # 1
            pass
        elif ((0 < len(self.calc_arr)) 
            and ('/' == self.calc_arr[-1])
            and ((self.write_number is None) or (0 == float(self.write_number)))
            ):
            return
        elif (('<' == self.operand)
            # and (self.previous_operand in 'w<-+*/%')
            and (self.previous_operand in 'w<-+*/%=')
            and (self.write_number is not None)
            ):
            if (self.label_display_comment.text[-1] in '-+*/%'):
                self.label_display_comment.text += self.label_display.text
        elif ('=' == self.operand) and ('*' == self.previous_operand):
            return
        elif ('w' != self.operand):
            return

        self.display_clear = True # 2

        self.previous_operand = self.operand # 3
        self.operand = '*' # 4

        self.label_display_comment.text += str(self.operand) # 5

        self.calc_arr.append(self.write_number) # 6
        self.calc_arr.append(self.operand)

        self.push_back = False # 7

        if (self.push_equal): # 8
            self.push_equal = False
            self.label_display_comment.text = self.write_number
            self.label_display_comment.text += str(self.operand)

        # 9
        self.label_display_comment.text = Parse().history_trim(self.label_display_comment.text,
                                                                limit_history)

        # test #########################################################
        print('------------------------------------------------') ######
        print(' multiply write_number =', self.write_number) ###########
        print(' multiply temp_number =', self.temp_number) #############
        print(' multiply result_number =', self.result_number) #########
        print(' multiply operand =', self.operand) #####################
        print(' multiply previous_operand =', self.previous_operand) ###
        print(' multiply calc_arr =', self.calc_arr) ###################
        print(' multiply zero =', self.zero) ###########################
        print(' multiply push_back =', self.push_back) #################
        print(' multiply push_equal =', self.push_equal) ###############
    # ---------------------------------------------------------------------------
    # операнд деления чисел
    # 1. условия проверки нажятия кнопки '/'
    # 2. пометить переменную display_clear в True
    # (при следующем вводе цифр очистить дисплей калькулятора)
    # 3. записываем в переменную previous_operand предыдущий операнд
    # 4. записываем в переменную operand текущий операнд
    # 5. записываем историю в label_display_comment
    # 6. записать в список (массив) итоговую переменную write_number и примененный operand
    # 7. пометить что кнопка back ('<') была не нажата
    # 8. если кнопка equal была нажата то пометить что она не была нажата (push_equal = False)
    # далее очистить и записать в историю label_display_comment ответ результата вычесления
    # и текущий операнд
    # 9. обрезать историю label_display_comment если она длинная
    def division(self):
        if ('=' == self.operand) and (self.previous_operand in 'w<'): # 1
            pass
        elif (('w' == self.operand) and (self.previous_operand is None)):
            pass
        elif ((0 < len(self.calc_arr)) 
            and ('/' == self.calc_arr[-1])
            and ((self.write_number is None) or (0 == float(self.write_number)))
            ):
            return  
        # elif ((('w' == self.operand) or ('<' == self.operand)) 
        #     and (self.previous_operand in '/w<')  
        #     and (self.zero)
        #     and (0 < len(self.calc_arr))
        #     ):
        #     self.zero = True
        #     return
        elif (('<' == self.operand)
            # and (self.previous_operand in 'w<-+*/%')
            and (self.previous_operand in 'w<-+*/%=')
            and (self.write_number is not None)
            ):
            if (self.label_display_comment.text[-1] in '-+*/%'):
                self.label_display_comment.text += self.label_display.text        
        elif ('=' == self.operand) and ('/' == self.previous_operand):
            return
        elif ('w' != self.operand):
            return

        self.display_clear = True # 2

        self.previous_operand = self.operand # 3
        self.operand = '/' # 4

        self.label_display_comment.text += str(self.operand) # 5

        self.calc_arr.append(self.write_number) # 6
        self.calc_arr.append(self.operand)

        self.push_back = False # 7

        if (self.push_equal): # 8
            self.push_equal = False
            self.label_display_comment.text = self.write_number
            self.label_display_comment.text += str(self.operand)

        # 9
        self.label_display_comment.text = Parse().history_trim(self.label_display_comment.text,
                                                                limit_history)

        # test #########################################################
        print('------------------------------------------------') ######
        print(' division write_number =', self.write_number) ###########
        print(' division temp_number =', self.temp_number) #############
        print(' division result_number =', self.result_number) #########
        print(' division operand =', self.operand) #####################
        print(' division previous_operand =', self.previous_operand) ###
        print(' division calc_arr =', self.calc_arr) ###################
        print(' division zero =', self.zero) ###########################
        print(' division push_back =', self.push_back) #################
        print(' division push_equal =', self.push_equal) ###############
    # ---------------------------------------------------------------------------
    # операнд процент от числа
    # 1. условия проверки нажятия кнопки '%'
    # 2. пометить переменную display_clear в True
    # (при следующем вводе цифр очистить дисплей калькулятора)
    # 3. записываем в переменную previous_operand предыдущий операнд
    # 4. записываем в переменную operand текущий операнд
    # 5. записываем историю в label_display_comment
    # 6. записать в список (массив) итоговую переменную write_number и примененный operand
    # 7. пометить что кнопка back ('<') была не нажата
    # 8. если кнопка equal была нажата то пометить что она не была нажата (push_equal = False)
    # далее очистить и записать в историю label_display_comment ответ результата вычесления
    # и текущий операнд
    # 9. обрезать историю label_display_comment если она длинная
    def percent(self):
        if ('=' == self.operand) and (self.previous_operand in 'w<'): # 1
            pass
        elif ((0 < len(self.calc_arr)) 
            and ('/' == self.calc_arr[-1])
            and ((self.write_number is None) or (0 == float(self.write_number)))
            ):
            return
        elif (('<' == self.operand)
            # and (self.previous_operand in 'w<-+*/%')
            and (self.previous_operand in 'w<-+*/%=')
            and (self.write_number is not None)
            ):
            if (self.label_display_comment.text[-1] in '-+*/%'):
                self.label_display_comment.text += self.label_display.text
        elif ('=' == self.operand) and ('*' == self.previous_operand):
            return
        elif ('w' != self.operand):
            return

        self.display_clear = True # 2

        self.previous_operand = self.operand # 3
        self.operand = '%' # 4

        self.label_display_comment.text += str(self.operand) # 5

        self.calc_arr.append(self.write_number) # 6
        self.calc_arr.append(self.operand)

        self.push_back = False # 7

        if (self.push_equal): # 8
            self.push_equal = False
            self.label_display_comment.text = self.write_number
            self.label_display_comment.text += str(self.operand)

        # 9
        self.label_display_comment.text = Parse().history_trim(self.label_display_comment.text,
                                                                limit_history)

        # test ########################################################
        print('------------------------------------------------') #####
        print(' percent write_number =', self.write_number) ###########
        print(' percent temp_number =', self.temp_number) #############
        print(' percent result_number =', self.result_number) #########
        print(' percent operand =', self.operand) #####################
        print(' percent previous_operand =', self.previous_operand) ###
        print(' percent calc_arr =', self.calc_arr) ###################
        print(' percent zero =', self.zero) ###########################
        print(' percent push_back =', self.push_back) #################
        print(' percent push_equal =', self.push_equal) ###############
    # ---------------------------------------------------------------------------
    # операнд сохранения числа в память калькулятора
    # 1. сохранить в память калькулятора число
    # иначе извлечь из памяти калькулятора число на дисплей калькулятора
    def memory(self):
        if ('' == self.label_display_memory.text) and ('' == self.label_display.text): # 1
            return
        elif (self.push_equal) and ('' != self.label_display_memory.text):
            self.label_display_comment.text = self.label_display_memory.text
            self.label_display.text = self.label_display_memory.text
            self.write_number = self.label_display_memory.text
            self.label_display_memory.text = ''
            self.push_equal = False
        elif ('' == self.label_display_memory.text) and ('' != self.label_display.text):
            self.label_display_memory.text = self.label_display.text
        else:  
            if ('' == self.label_display_comment.text):
                self.label_display_comment.text = self.label_display_memory.text  
            elif (((self.label_display_comment.text[-1] in '-+*/%')) 
                and (self.label_display_memory.text[0] in '-+*/%')):
                self.label_display_comment.text += self.label_display_memory.text
            elif ((self.label_display_comment.text[-1] in '-+*/%') 
                and (0 < len(Parse().split_with_operand_and_exponent(self.label_display_comment.text)))
                ):
                if (self.label_display_memory.text[0] not in '-+*/%'):
                    self.label_display_comment.text = Parse().back_to_operand(self.label_display_comment.text)
                    self.label_display_comment.text += self.label_display_memory.text
                else:
                    self.label_display_comment.text += self.label_display_memory.text
            elif ((self.label_display_comment.text[-1] not in '-+*/%') 
                and (1 < len(Parse().split_with_operand_and_exponent(self.label_display_comment.text)))
                ):
                if (self.label_display_memory.text[0] not in '-+*/%'):
                    self.label_display_comment.text = Parse().back_to_operand(self.label_display_comment.text)
                    self.label_display_comment.text += self.label_display_memory.text
                else:
                    self.label_display_comment.text = Parse().back_to_operand(self.label_display_comment.text)
                    if (self.label_display_comment.text[-1] in '+*/%'):
                        self.label_display_comment.text += self.label_display_memory.text
                    else:
                        if ('-' == self.label_display_comment.text[-2]):
                            self.label_display_comment.text = self.label_display_comment.text[: -1]
                            self.label_display_comment.text += self.label_display_memory.text
                        else:
                            self.label_display_comment.text += self.label_display_memory.text
            else:
                self.label_display_comment.text = self.label_display_memory.text
            self.label_display.text = self.label_display_memory.text
            self.write_number = self.label_display_memory.text
            self.operand = 'w'
            self.push_back = True
            self.label_display_memory.text = ''    

        # test #######################################################
        print('------------------------------------------------') ####
        print(' memory write_number =', self.write_number) ###########
        print(' memory temp_number =', self.temp_number) #############
        print(' memory result_number =', self.result_number) #########
        print(' memory operand =', self.operand) #####################
        print(' memory previous_operand =', self.previous_operand) ###
        print(' memory calc_arr =', self.calc_arr) ###################
        print(' memory zero =', self.zero) ###########################
        print(' memory push_back =', self.push_back) #################
        print(' memory push_equal =', self.push_equal) ###############
    # ---------------------------------------------------------------------------
    # операнд удаление чисел     
    # 1. удалить крайнюю цифру из числа
    # 2. записываем в переменную previous_operand предыдущий операнд
    # 3. записываем в переменную operand текущий операнд
    # 4. пометить что идет правильное деление (делить на ноль нельзя)
    # 5. пометить что кнопка back ('<') была нажата True
    # (в методах для операндов поставить False)
    # 6. если кнопка equal была нажата то пометить что она не была нажата (push_equal = False)
    # далее очистить и записать в историю label_display_comment ответ результата вычесления
    def back(self):
        if ('' == self.label_display.text): # 1
            return
        elif (self.label_display_comment.text[-1] in '-+*/%') and ('' == self.label_display.text):
            return
        elif ('e' in self.label_display.text) or ('E' in self.label_display.text):
            text_display = self.label_display.text
            text_display_comment = self.label_display_comment.text
            size_text_display = len(text_display)
            size_text_display_comment = len(text_display_comment)
            # if (text_display == text_display_comment.endswith(text_display)):
            if ((text_display == text_display_comment[size_text_display_comment - size_text_display : ]) 
                or (text_display[:] == text_display_comment[:])):
                if ((self.label_display.text[-1] in '0123456789') 
                    and (self.label_display.text[-2] in '0123456789')):
                    self.label_display.text = self.label_display.text[: -1]
                    self.label_display_comment.text = self.label_display_comment.text[: -1]
                elif ((self.label_display.text[-1] in '0123456789') 
                    and (self.label_display.text[-2] in '-+*/%')
                    and (self.label_display.text[-3] in 'eE')):
                    self.label_display.text = self.label_display.text[: -3]
                    self.label_display_comment.text = self.label_display_comment.text[: -3]
                self.write_number = None if 0 == len(self.label_display.text) else self.label_display.text            
            elif (self.operand in '-+*/%'):
                if ((self.label_display.text[-1] in '0123456789') 
                    and (self.label_display.text[-2] in '0123456789')):
                    digit_back = self.label_display.text[: -1]
                    self.label_display.text = digit_back
                    self.label_display_comment.text += digit_back
                elif ((self.label_display.text[-1] in '0123456789') 
                    and (self.label_display.text[-2] in '-+*/%')
                    and (self.label_display.text[-3] in 'eE')):
                    digit_back = self.label_display.text[: -3]
                    self.label_display.text = digit_back
                    self.label_display_comment.text += digit_back
                self.write_number = None if 0 == len(self.label_display.text) else self.label_display.text
        elif ((self.label_display_comment.text[0] in '-+*/%') 
            and (2 == len(self.label_display_comment.text))
            and (self.label_display.text[0] in '-+*/%')
            and (2 == len(self.label_display.text))
            ):
            self.label_display.text = ''
            self.label_display_comment.text = ''
            self.write_number = None
        elif ((self.label_display_comment.text[-1] in '-+*/%') 
            and (self.label_display.text[0] in '-+*/%')
            and (2 == len(self.label_display.text))
            ):
            self.label_display.text = ''
            self.write_number = None
        elif (('' != self.label_display_comment.text)
            and (self.label_display_comment.text[-1] in '-+*/%') 
            and (1 == len(self.label_display.text))
            ):
            self.label_display.text = ''
            self.write_number = None
        elif (('' != self.label_display_comment.text) 
            and (self.label_display_comment.text[-1] in '-+*/%')
            and (1 < len(self.label_display_comment.text))
            ): 
            self.label_display.text = self.label_display.text[: -1]
            # self.label_display_comment.text = Parse().back_to_operand(self.label_display_comment.text)           
            self.write_number = None if 0 == len(self.label_display.text) else self.label_display.text
            self.label_display_comment.text += self.write_number  
        elif (('' != self.label_display_comment.text)
            and (2 == len(self.label_display.text))
            and ('-' == self.label_display.text[0])
            ): 
            self.label_display_comment.text = Parse().back_to_operand(self.label_display_comment.text)
            self.label_display_comment.text = self.label_display_comment.text[: -1]
            self.label_display.text = ''
            self.write_number = None if 0 == len(self.label_display.text) else self.label_display.text
        elif (('' != self.label_display_comment.text) 
            and (self.label_display_comment.text[-1] in '-+*/%')
            and (1 < len(self.label_display.text))
            ): 
            self.label_display.text = self.label_display.text[: -1]
            # self.label_display_comment.text = Parse().back_to_operand(self.label_display_comment.text)           
            self.write_number = None if 0 == len(self.label_display.text) else self.label_display.text
            self.label_display_comment.text += self.write_number  
        elif ('' != self.label_display.text):
            self.label_display.text = self.label_display.text[: -1]
            self.write_number = None if 0 == len(self.label_display.text) else self.label_display.text
            self.label_display_comment.text = self.label_display_comment.text[: -1]
        elif (self.label_display.text is None):
            self.label_display.text = ''
        else:
            return

        self.previous_operand = self.operand # 2
        self.operand = '<' # 3

        if ('' != self.label_display.text) and (0 == float(self.label_display.text)): # 4
            self.zero = True
        else:
            self.zero = False

        self.push_back = True # 5

        if (self.push_equal): # 6
            self.push_equal = False
            if (self.write_number is None):
                self.label_display_comment.text = ''
            else:
                self.label_display_comment.text = self.write_number

        # test ######################################################
        print('------------------------------------------------') ###
        print(' back write_number =', self.write_number) ############
        print(' back temp_number =', self.temp_number) ##############
        print(' back result_number =', self.result_number) ##########
        print(' back operand =', self.operand) ######################
        print(' back previous_operand =', self.previous_operand) ####
        print(' back calc_arr =', self.calc_arr) ####################
        print(' back zero =', self.zero) ############################
        print(' back push_back =', self.push_back) ##################
        print(' back push_equal =', self.push_equal) ################
    # ---------------------------------------------------------------------------
    # операнд равно (результат действий калькулятора)
    # 1. условия проверки нажятия кнопки '='   
    # 2. записываем в переменную previous_operand предыдущий операнд
    # 3. записываем в переменную operand текущий операнд
    # 4. записать в список (массив) итоговую переменную write_number и примененный operand
    # 5. записать вычисления в историю
    # 6. выполнить вычисления выражения
    # 7. результат вычесления вывести на дисплей калькулятора (label_display)
    # 8. добавляем в историю label_display_comment текущий операнд
    # 9. результат вычесления добавить в историю калькулятора (label_display_comment)
    # 10. записываем в переменную write_number результат вычесления
    # 11. очищаем массив данных калькулятора calc_arr
    # 12. помечаем что кнопка equal была нажата (push_equal = True)
    # 13. обрезать историю label_display_comment если она длинная
    # 14. записать ответ вычислений в историю
    def equal(self):
        if (self.write_number is None) and (self.operand is None): # 1
            return
        elif (0 == len(self.calc_arr)):
            return
        elif (self.operand in '-+*/%='):
            return
        elif (self.label_display_comment.text[-1] in '-+*/%'):
            return
        elif (self.push_equal):
            return
        elif ((0 < len(self.calc_arr)) 
            and ('/' == self.calc_arr[-1])
            and ((self.write_number is None) or (0 == float(self.write_number)))
            ):
            return

        self.previous_operand = self.operand # 2
        self.operand = '=' # 3

        self.calc_arr.append(self.write_number) # 4
        self.calc_arr.append(self.operand)

        history_arr = Settings().load_history() # 5
        history_arr.append(''.join(self.calc_arr))

        res = str() # 6
        for i in self.calc_arr: 
            if (i in '-+*/%'):
                res += i
            elif ('=' == i):
                break
            else:
                res += i
                try:
                    op1 = Parse().back_to_operand_with_exponent(res)[-1]
                    op2 = Parse().back_to_operand_with_exponent(res)[-2]
                except (IndexError):
                    op1 = Parse().back_to_operand_with_exponent(res)[-1]
                    op2 = ''
                operand = op2 if op2 in '-+*/%' else op1
                round_str = Settings().load_settings()['round']
                round_str = Parse().round_decimal(int(round_str))

                if (('' != res) 
                    and (2 == len(Parse().split_with_operand_and_exponent(res)))
                    and ('%' == operand)
                    ):
                    # procent, digit = Parse().split(res)
                    # res = procent + '*' + digit + '/' + '100'
                    # res = str(eval(res))
                    a, b = Parse().split_with_operand_and_exponent(res)
                    procent, digit = Decimal(a), Decimal(b)
                    res = procent * digit / 100
                    if ('e' in str(res)) or ('E' in str(res)):
                        res = str(res)
                    else:
                        res = str(res.quantize(Decimal(round_str)))
                    res = Parse().del_ends_zero(res)
                else:
                    # res = str(eval(res))
                    if ('' != res) and (2 == len(Parse().split_with_operand_and_exponent(res))):
                        a, b = Parse().split_with_operand_and_exponent(res)
                        x, y = Decimal(a), Decimal(b)
                        if ('-' == operand):
                            res = x - y
                            if ('e' in str(res)) or ('E' in str(res)):
                                res = str(res)
                            else:
                                res = str(res.quantize(Decimal(round_str)))
                        elif ('+' == operand):
                            res = x + y
                            if ('e' in str(res)) or ('E' in str(res)):
                                res = str(res)
                            else:
                                res = str(res.quantize(Decimal(round_str)))
                        elif ('*' == operand):
                            res = x * y
                            if ('e' in str(res)) or ('E' in str(res)):
                                res = str(res)
                            else:
                                res = str(res.quantize(Decimal(round_str)))
                        elif ('/' == operand):
                            res = x / y
                            if ('e' in str(res)) or ('E' in str(res)):
                                res = str(res)
                            else:
                                res = str(res.quantize(Decimal(round_str)))
                        res = Parse().del_ends_zero(res)

        self.label_display.text = res # 7
        self.label_display_comment.text += str(self.operand) # 8
        self.label_display_comment.text += res # 9
        self.write_number = res # 10
        self.calc_arr.clear() # 11
        self.push_equal = True # 12

        # 13
        self.label_display_comment.text = Parse().history_trim(self.label_display_comment.text,
                                                                limit_history)

        history_arr[-1] += res # 14
        Settings().save_history(history_arr)

        # test ######################################################
        print('------------------------------------------------') ###
        print(' equal write_number =', self.write_number) ###########
        print(' equal temp_number =', self.temp_number) #############
        print(' equal result_number =', self.result_number) #########
        print(' equal operand =', self.operand) #####################
        print(' equal previous_operand =', self.previous_operand) ###
        print(' equal calc_arr =', self.calc_arr) ###################
        print(' equal zero =', self.zero) ###########################
        print(' equal push_back =', self.push_back) #################
        print(' equal res =', res) ##################################
        print(' equal push_equal =', self.push_equal) ###############
    # ---------------------------------------------------------------------------
    # обнудить все переменные при нажатии кнопки 'C'
    def clear(self):
        self.label_display.text = ''
        self.label_display_comment.text = ''
        # self.label_display_memory.text = ''
        self.display_clear = False
        self.push_back = False
        self.push_equal = False
        self.zero = False
        self.write_number = None
        self.temp_number = float()
        self.result_number = float()
        self.operand = None
        self.previous_operand = None
        self.calc_arr = list()

        # test ######################################################
        print('------------------------------------------------') ###
        print(' clear write_number =', self.write_number) ###########
        print(' clear temp_number =', self.temp_number) #############
        print(' clear result_number =', self.result_number) #########
        print(' clear operand =', self.operand) #####################
        print(' clear previous_operand =', self.previous_operand) ###
        print(' clear calc_arr =', self.calc_arr) ###################
        print(' clear zero =', self.zero) ###########################
        print(' clear push_back =', self.push_back) #################
        print(' clear push_equal =', self.push_equal) ###############
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# Модальное окно программы
# Если нет прав доступа на чтение и запись
# будет выведено это окно
class WindowAccess(BoxLayout):
    pass
# *****************************************************************************************
# Окно программы
class CalcApp(App, Design, Hardware):
    # ---------------------------------------------------------------------------
    '''app widget'''
    # ---------------------------------------------------------------------------
    # vars
    is_android = BooleanProperty(os_is_android)
    # setting_round = StringProperty(Settings().load_settings()['round'])
    # setting_hist = StringProperty(Settings().load_settings()['hist'])
    # setting_vibro = StringProperty(Settings().load_settings()['vibro'])
    # ---------------------------------------------------------------------------
    # kivy vars
    title = 'Kivy Calc'
    # ---------------------------------------------------------------------------
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # проверка существования файла настроек и истории json
        if (is_access_open):
            if not (file.file_exists_dir('./json/', __file__)):
                file.file_create_dir('./json/', __file__)
            if not (file.file_exists('./json/settings.json', __file__)):
                Settings().update_settings(round='2', hist='999', vibro='0.05')
            if not (file.file_exists('./json/history.json', __file__)):
                Settings().update_history()
    # ---------------------------------------------------------------------------
    def build(self):
        # если права доступа н открыты то показать WindowAccess
        # иначе запустить калькулятор
        if not (is_access_open):
            # filename = str(Path(join(dirname(__file__), './design/WindowAccess.kv')))
            # return Builder.load_file(filename)
            return WindowAccess()
        else:
            return Calc()
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    CalcApp().run()
# *****************************************************************************************