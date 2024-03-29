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
    # если в строке есть операнд '+-*/%'
    # то обрезать конец строки до последнего операнда учитывая числа с e(E)
    def back_to_operand_with_exponent(self, line: str) -> str:
        index = None
        i = len(line) - 1
        while 0 <= i:
            if (i == len(line) - 1) and (line[i] in '+-*/%'):
                pass
            elif (line[i] in '+-*/%') and (0 <= i - 1) and (line[i - 1] in 'eE'):
                pass
            elif (line[i] in '+-*/%'):
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
            elif (line[i] in '+-*/%='):
                index = i
                break
            i += 1
        if index is None: return line
        else: return line[index : ]
    # ---------------------------------------------------------------------------
    # если в строке есть операнд '+-*/%' или '+-*/%=' (на выбор)
    # то обрезать начало строки до первого операнда учитывая числа с e(E)
    def next_to_operand_with_exponent(self, line: str) -> str:
        index = None
        i = int()
        while i < len(line):
            if (0 ==i) and (line[i] in '+-*/%'):
                pass
            elif (line[i] in 'eE'):
                i += 2
                continue
            # elif line[i] in '+-*/%':
            elif (line[i] in '+-*/%='):
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
            if (line[i] in '.0123456789'):
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
                    if (line[left] in '.0123456789') and (1 == cnt):
                        cnt = int()
                        left += 2
                        break
                    if (line[left] in '.0123456789') and (0 == cnt) and (0 == left):
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
            if (line[i] in '.0123456789'):
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
                    if (line[left] in '.0123456789') and (1 == cnt):
                        cnt = int()
                        left += 2
                        break
                    if (line[left] in '.0123456789') and (0 == cnt) and (0 == left):
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
            line = self.next_to_operand_with_exponent(line)
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
    # конвертация целого числа для округления чисел типа Decimal
    def round_decimal(self, digit: int) -> str:
        res = '0' * digit
        return '1.' + res
    # ---------------------------------------------------------------------------
    # если число float и оно не дробное (целое) 
    # то удалить точку и все нули после нее
    def del_ends_zero(self, digit: str) -> str:
        idx = digit.find('.')

        if not (-1 == idx):
            line = digit[idx + 1 : ]
            for i in line:
                if '0' == i: continue
                else: break
            else:
                return digit[ : idx]

        if not (-1 == idx):
            while True:
                if ('0' == digit[-1]):
                    digit = digit[: -1]
                else:
                    return digit
                    
        return digit
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
    test_16_0 = '---22222'
    test_16_1 = '444444=6666666'
    test_16_2 = '+6767676=1.23456789012345678901234567890123456789012345678901234567890'
    test_16_3 = '-1212E+34--67676e+54-'
    test_16_4 = '-1212E+34--67676e+54'
    test_16_5 = '5.-2'
    test_16_6 = '-5.-2'
    test_16_7 = '-5.--2'
    test_16_8 = '5.*2'
    test_16_9 = '-5.*2'
    test_16_10 = '-5.*-2'
    test_16_11 = '5.+2'

    test_17 = '-1111+334343%2323232-232323+6767676=12345678901234567890'
    test_18 = '-1111+334343%2323232-232323+6767676=1.23456789012345678901234567890123456789012345678901234567890'
    test_19 = '-1111+334343%2323232-232323+6767676=123456789012345678901234567890123456789012345678901234567890'
    test_20 = '-1111+334343%2323232-232323+6767676=-123456789012345678901234567890123456789012345678901234567890'
    test_21 = '-1111+334343%2323232-232323+6767676=-1.00000000000000000000000000000000000000000000000000000000890'
    test_21_1 = '-1111E+28+334343e-76554%2323232E+676-232323+6767676=-12345678901234'
    test_21_2 = '-1111E+28+-334343e-76554%-2323232E+676--232323+-6767676=-12345678901234'
    test_21_3 = '12345678901234123456678912345678123345667898123456789123456789*'

    test_22 = '-12128989898+676767E+34--99999e-27/44444'

    test_23 = 1
    test_24 = 2
    test_25 = 5

    test_26 = '5.000'
    test_27 = '6.001'
    test_28 = '6.400'
    test_29 = '6.050'

    print('-------------------------------------')
    print('back_to_operand')

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
    print(Parse().back_to_operand(test_16_0))
    print(Parse().back_to_operand(test_16_1))
    print(Parse().back_to_operand(test_16_2))
    print(Parse().back_to_operand(test_16_3))
    print(Parse().back_to_operand(test_16_4))
    print(Parse().back_to_operand(test_16_5))

    print('-------------------------------------')
    print('back_to_operand_with_exponent')

    print(Parse().back_to_operand_with_exponent(test_1))
    print(Parse().back_to_operand_with_exponent(test_2))
    print(Parse().back_to_operand_with_exponent(test_3))
    print(Parse().back_to_operand_with_exponent(test_4))
    print(Parse().back_to_operand_with_exponent(test_5))
    print(Parse().back_to_operand_with_exponent(test_6))
    print(Parse().back_to_operand_with_exponent(test_7))
    print(Parse().back_to_operand_with_exponent(test_8))
    print(Parse().back_to_operand_with_exponent(test_9))
    print(Parse().back_to_operand_with_exponent(test_10))
    print(Parse().back_to_operand_with_exponent(test_11))
    print(Parse().back_to_operand_with_exponent(test_12))
    print(Parse().back_to_operand_with_exponent(test_13))
    print(Parse().back_to_operand_with_exponent(test_14))
    print(Parse().back_to_operand_with_exponent(test_15))
    print(Parse().back_to_operand_with_exponent(test_16))
    print(Parse().back_to_operand_with_exponent(test_16_0))
    print(Parse().back_to_operand_with_exponent(test_16_1))
    print(Parse().back_to_operand_with_exponent(test_16_2))
    print(Parse().back_to_operand_with_exponent(test_16_3))
    print(Parse().back_to_operand_with_exponent(test_16_4))
    print(Parse().back_to_operand_with_exponent(test_16_5))
    print(Parse().back_to_operand_with_exponent(test_16_6))
    print(Parse().back_to_operand_with_exponent(test_16_7))
    print(Parse().back_to_operand_with_exponent(test_16_8))
    print(Parse().back_to_operand_with_exponent(test_16_9))
    print(Parse().back_to_operand_with_exponent(test_16_10))

    print('-------------------------------------')
    print('split')

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
    print('split_with_operand')

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
    print('split_with_operand_and_exponent')
  
    print(Parse().split_with_operand_and_exponent(test_1))
    print(Parse().split_with_operand_and_exponent(test_2))
    print(Parse().split_with_operand_and_exponent(test_3))
    print(Parse().split_with_operand_and_exponent(test_4))
    print(Parse().split_with_operand_and_exponent(test_5))
    print(Parse().split_with_operand_and_exponent(test_6))
    print(Parse().split_with_operand_and_exponent(test_7))
    print(Parse().split_with_operand_and_exponent(test_8))
    print(Parse().split_with_operand_and_exponent(test_9))
    print(Parse().split_with_operand_and_exponent(test_10))
    print(Parse().split_with_operand_and_exponent(test_11))
    print(Parse().split_with_operand_and_exponent(test_12))
    print(Parse().split_with_operand_and_exponent(test_13))
    print(Parse().split_with_operand_and_exponent(test_14))
    print(Parse().split_with_operand_and_exponent(test_15))
    print(Parse().split_with_operand_and_exponent(test_16))
    print(Parse().split_with_operand_and_exponent(test_16_1))
    print(Parse().split_with_operand_and_exponent(test_16_2))
    print(Parse().split_with_operand_and_exponent(test_16_3))
    print(Parse().split_with_operand_and_exponent(test_16_4))
    print(Parse().split_with_operand_and_exponent(test_16_5))
    print(Parse().split_with_operand_and_exponent(test_16_6))
    print(Parse().split_with_operand_and_exponent(test_16_7))
    print(Parse().split_with_operand_and_exponent(test_16_8))
    print(Parse().split_with_operand_and_exponent(test_16_9))
    print(Parse().split_with_operand_and_exponent(test_16_10))
    print(Parse().split_with_operand_and_exponent(test_16_11))
    print('*************************************')
    print(test_22)
    print(Parse().split_with_operand_and_exponent(test_22))

    print('-------------------------------------')
    print('next_to_operand')

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
    print(Parse().next_to_operand(test_16_3))

    print('-------------------------------------')
    print('next_to_operand_with_exponent')

    print(Parse().next_to_operand_with_exponent(test_1))
    print(Parse().next_to_operand_with_exponent(test_2))
    print(Parse().next_to_operand_with_exponent(test_3))
    print(Parse().next_to_operand_with_exponent(test_4))
    print(Parse().next_to_operand_with_exponent(test_5))
    print(Parse().next_to_operand_with_exponent(test_6))
    print(Parse().next_to_operand_with_exponent(test_7))
    print(Parse().next_to_operand_with_exponent(test_8))
    print(Parse().next_to_operand_with_exponent(test_9))
    print(Parse().next_to_operand_with_exponent(test_10))
    print(Parse().next_to_operand_with_exponent(test_11))
    print(Parse().next_to_operand_with_exponent(test_12))
    print(Parse().next_to_operand_with_exponent(test_13))
    print(Parse().next_to_operand_with_exponent(test_14))
    print(Parse().next_to_operand_with_exponent(test_15))
    print(Parse().next_to_operand_with_exponent(test_16))
    print(Parse().next_to_operand_with_exponent(test_16_0))
    print(Parse().next_to_operand_with_exponent(test_16_1))
    print(Parse().next_to_operand_with_exponent(test_16_2))
    print(Parse().next_to_operand_with_exponent(test_16_3))

    print('-------------------------------------')
    print('history_trim')

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
    print('*************************************')
    print(test_21_1)
    print(Parse().history_trim(test_21_1, 50))
    print('*************************************')
    print(test_21_2)
    print(Parse().history_trim(test_21_2, 50))
    print('*************************************')
    print(test_21_3)
    print(Parse().history_trim(test_21_3, 50))

    print('-------------------------------------')
    print('round_decimal')

    print(Parse().round_decimal(test_23))
    print(Parse().round_decimal(test_24))
    print(Parse().round_decimal(test_25))

    print('-------------------------------------')
    print('round_decimal')

    print(Parse().del_ends_zero(test_26))
    print(Parse().del_ends_zero(test_27))
    print(Parse().del_ends_zero(test_28))
    print(Parse().del_ends_zero(test_29))

    print('-------------------------------------')
# *****************************************************************************************