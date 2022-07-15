# *****************************************************************************************
# re - импорт регулярных выражений
import re
# *****************************************************************************************
# Parse - разбор текстовых строк
class Parse:
    # ---------------------------------------------------------------------------
    # если в строке есть операнд '+-*/%'
    # то обрезать конец строки до последнего операнда
    def back_to_operand(self, line: str) -> str:
        index = None
        i = len(line) - 1
        while 0 <= i:
            if line[i] in '+-*/%':
                index = i
                break
            i -= 1
        if index is None: return line
        else: return line[: index + 1]
    # ---------------------------------------------------------------------------
    def next_to_operand(self):
        pass
    # ---------------------------------------------------------------------------
    # разделение строки по разделителям '+-*/%'
    def split(self, line: str) -> list[str]:
        arr = re.split('\+|\-|\*|\/|\%', line)
        if '' == arr[0]:
            arr[1] = line[0] + arr[1]
        return arr if '' != arr[0] else arr[1 : ]
    # ---------------------------------------------------------------------------
    def validate_history(self):
        pass
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    test_1 = '1212+67676-787878+8989898'
    test_2 = '1212+67676-787878%8989898'
    test_3 = '1212+67676-787878-8989898'
    test_4 = '1212+67676-787878/8989898'
    test_5 = '1212+67676-787878*8989898'
    test_6 = '12128989898'
    test_7 = '-12128989898'
    test_8 = '-12128989898+676767-99999'
    test_9 = '-12128989898--99999-88888'

    print(Parse().back_to_operand(test_1))
    print(Parse().back_to_operand(test_2))
    print(Parse().back_to_operand(test_3))
    print(Parse().back_to_operand(test_4))
    print(Parse().back_to_operand(test_5))
    print(Parse().back_to_operand(test_6))
    print(Parse().back_to_operand(test_7))
    print(Parse().back_to_operand(test_8))
    print(Parse().back_to_operand(test_9))

    print(Parse().split(test_1))
    print(Parse().split(test_2))
    print(Parse().split(test_3))
    print(Parse().split(test_4))
    print(Parse().split(test_5))
    print(Parse().split(test_6))
    print(Parse().split(test_7))
    print(Parse().split(test_8))
    print(Parse().split(test_9))
# *****************************************************************************************