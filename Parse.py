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
    # если в строке есть операнд '+-*/%' или '+-*/%=' (на выбор)
    # то обрезать начало строки до первого операнда
    def next_to_operand(self, line: str) -> str:
        index = None
        i = int()
        while i < len(line):
            if (0 ==i) and (line[i] in '+-*/%'):
                pass
            # elif line[i] in '+-*/%':
            elif line[i] in '+-*/%=':
                index = i
                break
            i += 1
        if index is None: return line
        else: return line[index : ]
    # ---------------------------------------------------------------------------
    # разделение строки по разделителям '+-*/%'
    def split(self, line: str) -> list[str]:
        arr = re.split('\+|\-|\*|\/|\%', line)
        if '' == arr[0]:
            del arr[0]
        
        if '' in arr:
            i = int()
            while i < len(arr):
                if ('' == arr[i]):
                    del arr[i]
                    i -= 1
                i += 1

        return arr
    # ---------------------------------------------------------------------------
    # разделение строки по разделителям '+-*/%' игнорируя отрицательные числа
    def split_with_operand(self, line: str) -> list[str]:
        arr = list()
        size_line = len(line)
        i = int()

        while i < size_line:
            if (line[i].isdigit()):
                left = i
                right = i
                cnt = int()
                while 0 <= left:
                    if (line[left] in '+-*/%'):
                        cnt += 1
                    if (line[left] in '+-*/%') and (2 == cnt):
                        cnt = int()
                        left += 1
                        break
                    if (line[left] in '+-*/%') and (1 == cnt) and (0 == left):
                        cnt = int()
                        break
                    if (line[left].isdigit()) and (1 == cnt):
                        cnt = int()
                        left += 2
                        break
                    if (line[left].isdigit()) and (0 == cnt) and (0 == left):
                        break
                    left -= 1
                while right < size_line:
                    if (line[right] in '+-*/%'):
                        break
                    right += 1
                arr.append(line[left : right])
                i = right - 1
            i += 1

        return arr
    # ---------------------------------------------------------------------------
    # разделение строки по разделителям '+-*/%' игнорируя отрицательные числа
    # также учитывая числа с эксонентой e(E) т.е. число в степени
    def split_with_operand_and_exponent(self, line: str) -> list[str]:
        arr = list()
        size_line = len(line)
        i = int()

        while i < size_line:
            if (line[i].isdigit()):
                left = i
                right = i
                cnt = int()
                while 0 <= left:
                    if (line[left] in '+-*/%'):
                        cnt += 1
                    if (line[left] in '+-*/%') and (2 == cnt):
                        cnt = int()
                        left += 1
                        break
                    if (line[left] in '+-*/%') and (1 == cnt) and (0 == left):
                        cnt = int()
                        break
                    if (line[left].isdigit()) and (1 == cnt):
                        cnt = int()
                        left += 2
                        break
                    if (line[left].isdigit()) and (0 == cnt) and (0 == left):
                        break
                    left -= 1
                while right < size_line:
                    if (line[right] in 'eE'):
                        right +=2
                        continue
                    elif (line[right] in '+-*/%'):
                        break
                    right += 1
                arr.append(line[left : right])
                i = right - 1
            i += 1

        return arr
    # ---------------------------------------------------------------------------
    # обрезка истории, если не помещается на дисплей калькулятора
    # (с начала строки обрезаются дейстаия до первого операнда,
    # если ответ большой то он сокращается,
    # лимит длинны строки на android = 100 символов,
    # остальные ОС = 40 символов)
    def history_trim(self, line: str, limit: int) -> str:
        i = limit-1

        while (len(line) > limit):
            line = self.next_to_operand(line)
            if (line[0] in '='):
                if(line[0] in '='):
                    line = line[1 : ]
                while (len(line) > limit):
                    line_digit = float(line)
                    line_digit = round(line_digit, i)
                    line = str(line_digit)
                    i -= 1

        return line
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
    test_10 = '12128989898--99999-88888'
    test_11 = '12128989898--99999------88888'
    test_12 = '12128989898--99999------88888-'
    test_13 = '12128989898--99999------88888----'
    test_14 = '-654%-5'
    test_15 = '-555555---'
    test_16 = '-'
    test_16_1 = '444444=6666666'
    test_16_2 = '+6767676=1.23456789012345678901234567890123456789012345678901234567890'

    test_17 = '-1111+334343%2323232-232323+6767676=12345678901234567890'
    test_18 = '-1111+334343%2323232-232323+6767676=1.23456789012345678901234567890123456789012345678901234567890'
    test_19 = '-1111+334343%2323232-232323+6767676=123456789012345678901234567890123456789012345678901234567890'
    test_20 = '-1111+334343%2323232-232323+6767676=-123456789012345678901234567890123456789012345678901234567890'
    test_21 = '-1111+334343%2323232-232323+6767676=-1.00000000000000000000000000000000000000000000000000000000890'
    
    test_22 = '-12128989898+676767E+34--99999e-27/44444'

    print(Parse().back_to_operand(test_1))
    print(Parse().back_to_operand(test_2))
    print(Parse().back_to_operand(test_3))
    print(Parse().back_to_operand(test_4))
    print(Parse().back_to_operand(test_5))
    print(Parse().back_to_operand(test_6))
    print(Parse().back_to_operand(test_7))
    print(Parse().back_to_operand(test_8))
    print(Parse().back_to_operand(test_9))
    print(Parse().back_to_operand(test_10))
    print(Parse().back_to_operand(test_11))
    print(Parse().back_to_operand(test_12))
    print(Parse().back_to_operand(test_13))
    print(Parse().back_to_operand(test_14))
    print(Parse().back_to_operand(test_15))
    print(Parse().back_to_operand(test_16))
    print(Parse().back_to_operand(test_16_1))
    print(Parse().back_to_operand(test_16_2))

    print('-------------------------------------')

    print(Parse().split(test_1))
    print(Parse().split(test_2))
    print(Parse().split(test_3))
    print(Parse().split(test_4))
    print(Parse().split(test_5))
    print(Parse().split(test_6))
    print(Parse().split(test_7))
    print(Parse().split(test_8))
    print(Parse().split(test_9))
    print(Parse().split(test_10))
    print(Parse().split(test_11))
    print(Parse().split(test_12))
    print(Parse().split(test_13))
    print(Parse().split(test_14))
    print(Parse().split(test_15))
    print(Parse().split(test_16))
    print(Parse().split(test_16_1))
    print(Parse().split(test_16_2))

    print('-------------------------------------')

    print(Parse().split_with_operand(test_1))
    print(Parse().split_with_operand(test_2))
    print(Parse().split_with_operand(test_3))
    print(Parse().split_with_operand(test_4))
    print(Parse().split_with_operand(test_5))
    print(Parse().split_with_operand(test_6))
    print(Parse().split_with_operand(test_7))
    print(Parse().split_with_operand(test_8))
    print(Parse().split_with_operand(test_9))
    print(Parse().split_with_operand(test_10))
    print(Parse().split_with_operand(test_11))
    print(Parse().split_with_operand(test_12))
    print(Parse().split_with_operand(test_13))
    print(Parse().split_with_operand(test_14))
    print(Parse().split_with_operand(test_15))
    print(Parse().split_with_operand(test_16))
    print(Parse().split_with_operand(test_16_1))
    print(Parse().split_with_operand(test_16_2))

    print('-------------------------------------')

    print(Parse().next_to_operand(test_1))
    print(Parse().next_to_operand(test_2))
    print(Parse().next_to_operand(test_3))
    print(Parse().next_to_operand(test_4))
    print(Parse().next_to_operand(test_5))
    print(Parse().next_to_operand(test_6))
    print(Parse().next_to_operand(test_7))
    print(Parse().next_to_operand(test_8))
    print(Parse().next_to_operand(test_9))
    print(Parse().next_to_operand(test_10))
    print(Parse().next_to_operand(test_11))
    print(Parse().next_to_operand(test_12))
    print(Parse().next_to_operand(test_13))
    print(Parse().next_to_operand(test_14))
    print(Parse().next_to_operand(test_15))
    print(Parse().next_to_operand(test_16))
    print(Parse().next_to_operand(test_16_1))
    print(Parse().next_to_operand(test_16_2))

    print('-------------------------------------')

    print(test_17)
    print(Parse().history_trim(test_17, 50))
    print('*************************************')
    print(test_18)
    print(Parse().history_trim(test_18, 50))
    print('*************************************')
    print(test_19)
    print(Parse().history_trim(test_19, 50))
    print('*************************************')
    print(test_20)
    print(Parse().history_trim(test_20, 50))
    print('*************************************')
    print(test_21)
    print(Parse().history_trim(test_21, 50))

    print('-------------------------------------')

    print(test_22)
    print(Parse().split_with_operand_and_exponent(test_22))

# *****************************************************************************************