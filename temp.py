for i in range(10):
    print(f'{i} = {chr(i)}')
print('---------------------------')
print(chr(183))
print('---------------------------')
print('float("09") =', float(" 09"))
# print('float("") =', float(""))
print('eval(100 % 50) =', eval('10 % 50'))
print('---------------------------')
# print("float('-'): " ,float('-'))
print("float('-0'): " ,float('-0'))
# print("float('.'): " ,float('.'))
print('---------------------------')
if -0.0:
    print(True)
else:
    print(False)
print('---------------------------')
if -0.0 == 0:
    print(True)
else:
    print(False)
print('---------------------------')
print("float('0.'): " ,float('0.'))
print('---------------------------')
a = ''
print('a =' , a)
print('---------------------------')
print("float('-0.'): " ,float('-0.'))
print('---------------------------')
import re
my_st = "Я\nучу; язык,программирования\nPython"
print(re.split(';|,|\n', my_st)[-1])
print('---------------------------')
import re
my_st = "Я учу язык программирования Python"
print(re.split(';|,|\n', my_st)[-1])
print('---------------------------')
class Parse:
    def split(self, line: str) -> list[str]:
        import re
        return re.split('\+|\-|\*|\/|\%', line)

print(Parse().split('1212+67676-787878+8989898'))
print('---------------------------')
res = '50 % 10'
res = eval(res)
print('res =', res)
print('type(res) =', type(res))
print('---------------------------')
print('123456789'[-2])
print('---------------------------')
from decimal import Decimal
a = Decimal('-5')
b = Decimal('15')
print(a + b)
print('---------------------------')
line = '-+*/='
print('1212+7878784-3434/676767*676767'.count(line))
print(''.count.__doc__)
print('---------------------------')
print(round(1.3435446, 3))
print('---------------------------')
# 3435442323232323
print(round(1.34354423232323232323232323454567767879890909454561212234354667687898090, 40))
print('---------------------------')
print(round(12345678901234567890123456789012345343434345565676766789012345678901234567890, 50))
print('---------------------------')
s1 = 'ggggg666'
s2 = '666'
size_s1 =len(s1)
size_s2 =len(s2)
if (s2 == s1[size_s1 - size_s2 -1 : ]):
    print('концы строк равны')
else:
    print('концы строк равны')
print('---------------------------')
s1 = 'ggggg666'
s2 = '666'
if (s2 == s1.endswith(s2)):
    print('концы строк равны')
else:
    print('концы строк равны')
print('---------------------------')
# print('12345'[: -1])
print('---------------------------')
print('12345'[: -3])
print('---------------------------')
s1 = '666'
s2 = '666'
if (s2 == s1.endswith(s2)):
    print('концы строк равны')
else:
    print('концы строк равны')
print('---------------------------')
print('12345'[:])
print('---------------------------')
a = '678788934546568783434343445989676232343334454545454545656454566344556677845566774555667678'
print(f'a = {a}')
print(f'float(a) = {float(a)}')
a = float(a)
print(f'a = {a}')
print('---------------------------')
from decimal import Decimal
a, b = Decimal('-5.'), Decimal('5.')
print(f'a = {a}')
print(f'b = {b}')
print(f'a * b = {a * b}')
print('---------------------------')
# exit()
print('если этого не видно то был выход')
print('---------------------------')
from math import floor, ceil
from decimal import Decimal
a, b = Decimal('567E+10'), Decimal('53434E+16')
c = a * b
# d = c.quantize(Decimal('1.000'))
e = float(c)
g = ceil(c)
# k = c.quantize(Decimal('1.000'))
print(f'a = {a}')
print(f'b = {b}')
print(f'c = a * b = {c}')
# print(f'd = {d}')
print(f'e = {e}')
print(f'g = {g}')
# print(f'k = {k}')
q = Decimal('55E+12')
print(f'type =  {type(q)}')
print(f'q =  {q}')
print(f'str(q) =  {str(q)}')
print('---------------------------')