print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')
print('|', '', '', '', '', '', '', '|', '', '', '', '', '', '', '|')
print('|', '', '', '', '', '', '', '|', '', '', '', '', '', '', '|')
print('|', '', '', '', '', '', '', '|', '', '', '', '', '', '', '|')
print('|', '', '', '', '', '', '', '|', '', '', '', '', '', '', '|')
print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')
print('|', '', '', '', '', '', '', '|', '', '', '', '', '', '', '|')
print('|', '', '', '', '', '', '', '|', '', '', '', '', '', '', '|')
print('|', '', '', '', '', '', '', '|', '', '', '', '', '', '', '|')
print('|', '', '', '', '', '', '', '|', '', '', '', '', '', '', '|')
print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')

print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')
print('|', '-', '-', '-', '-', '|', '-', '-', '-', '-', '|')
print('|', '-', '-', '-', '-', '|', '-', '-', '-', '-', '|')
print('|', '-', '-', '-', '-', '|', '-', '-', '-', '-', '|')
print('|', '-', '-', '-', '-', '|', '-', '-', '-', '-', '|')
print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')
print('|', '-', '-', '-', '-', '|', '-', '-', '-', '-', '|')
print('|', '-', '-', '-', '-', '|', '-', '-', '-', '-', '|')
print('|', '-', '-', '-', '-', '|', '-', '-', '-', '-', '|')
print('|', '-', '-', '-', '-', '|', '-', '-', '-', '-', '|')
print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')

def new_grid(a=3, b=4):
    border = '+' + b * (' ' + '-' + ' ')
    body = '|' + b * 3 * (' ')
    for i in range(a):
        print(a * border + '+')
        for i in range(b):
            print(body * a + '|')
    print (a * border + '+')

new_grid()

for x in list(range(0,100)):
output = ""
if(x % 3 == 0):
output += 'Fizz'
if(x % 5 == 0):
output += 'Buzz'
if(output == ""):
output += str(x)

print(output)

>>> >>> for num in range(1,21):
...     string = ""
...     if num % 3 == 0:
...         string = string + "Fizz"
...     if num % 5 == 0:
...         string = string + "Buzz"
...     if num % 5 != 0 and num % 3 != 0:
...         string = string + str(num)
...     print(string)


>>> for num in range(1,100):
...     string = ""
...     if num % 3 == 0:
...         string = string + "Fizz"
...     if num % 5 == 0:
...         string = string + "Buzz"
...     if num % 5 != 0 and num % 3 != 0:
...         string = string + str(num)
...     print(string)
for num in range(1,100):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)