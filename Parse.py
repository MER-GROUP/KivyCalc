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
    test_10 = '12128989898--99999-88888'
    test_11 = '12128989898--99999------88888'
    test_12 = '12128989898--99999------88888-'
    test_13 = '12128989898--99999------88888----'
    test_14 = '-654%-5'

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

# *****************************************************************************************