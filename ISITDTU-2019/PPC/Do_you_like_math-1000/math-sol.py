from pwn import *

def translate(arr):

    zero =[[' ',' ','#','#','#',' ',' '],
           [' ','#',' ',' ',' ','#',' '],
           ['#',' ',' ',' ',' ',' ','#'],
           ['#',' ',' ',' ',' ',' ','#'],
           ['#',' ',' ',' ',' ',' ','#'],
           [' ','#',' ',' ',' ','#',' '],
           [' ',' ','#','#','#',' ',' ']]

    one = [[' ',' ','#',' ',' ',' ','#'],
           [' ','#',' ',' ',' ',' ','#'],
           ['#','#','#','#','#','#','#'],
           [' ',' ',' ',' ',' ',' ','#'],
           [' ',' ',' ',' ',' ',' ','#']]

    two = [[' ','#',' ',' ','#','#','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           [' ','#','#',' ',' ',' ','#']]

    three=[[' ','#',' ',' ',' ','#',' '],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           [' ','#','#',' ','#','#',' ']]

    four =[['#','#','#','#','#',' ',' '],
           [' ',' ',' ',' ','#',' ',' '],
           [' ',' ',' ',' ','#',' ',' '],
           [' ',' ',' ',' ','#',' ',' '],
           [' ',' ',' ',' ','#',' ',' '],
           [' ','#','#','#','#','#','#'],
           [' ',' ',' ',' ','#',' ',' ']]

    five =[['#','#','#','#',' ','#',' '],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ',' ','#','#',' ']]

    six = [[' ','#','#','#','#','#',' '],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           [' ','#',' ',' ','#','#',' ']]

    seven=[['#','#',' ',' ',' ',' ',' '],
           ['#',' ',' ',' ',' ',' ',' '],
           ['#',' ',' ',' ','#','#','#'],
           ['#',' ',' ','#',' ',' ',' '],
           ['#',' ','#',' ',' ',' ',' '],
           ['#','#',' ',' ',' ',' ',' '],
           ['#',' ',' ',' ',' ',' ',' ']]

    eight=[[' ','#','#',' ','#','#',' '],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           [' ','#','#',' ','#','#',' ']]

    nine =[[' ','#','#',' ',' ','#',' '],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           ['#',' ',' ','#',' ',' ','#'],
           [' ','#','#','#','#','#',' ']]

    add = [[' ',' ',' ','#',' ',' ',' '],
           [' ',' ',' ','#',' ',' ',' '],
           [' ','#','#','#','#','#',' '],
           [' ',' ',' ','#',' ',' ',' '],
           [' ',' ',' ','#',' ',' ',' ']]

    sub = [[' ',' ',' ','#',' ',' ',' '],
           [' ',' ',' ','#',' ',' ',' '],
           [' ',' ',' ','#',' ',' ',' '],
           [' ',' ',' ','#',' ',' ',' '],
           [' ',' ',' ','#',' ',' ',' ']]

    mult =[[' ',' ',' ','#',' ',' ',' '],
           [' ','#',' ','#',' ','#',' '],
           [' ',' ','#','#','#',' ',' '],
           [' ',' ',' ','#',' ',' ',' '],
           [' ',' ','#','#','#',' ',' '],
           [' ','#',' ','#',' ','#',' '],
           [' ',' ',' ','#',' ',' ',' ']]
    div = [[' ',' ',' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ',' ',' ']]
    if arr == zero:
        return '0'
    elif arr == one:
        return '1'
    elif arr == two:
        return '2'
    elif arr == three:
        return '3'
    elif arr == four:
        return '4'
    elif arr == five:
        return '5'
    elif arr == six:
        return '6'
    elif arr == seven:
        return '7'
    elif arr == eight:
        return '8'
    elif arr == nine:
        return '9'
    elif arr == add:
        return '+'
    elif arr == sub:
        return '-'
    elif arr == mult:
        return '*'
r = remote('104.154.120.223',8083)
countN = 0
while True:
    equation = ''
    r.recvline()
    arr = []
    for i in range(7):
        try:
            s = r.recvline()
        except EOFError:
            r.interactive()
        arr.append(s[:-1])
    arr_num = []
    for i in range(50):
        arr2 =[row[i] for row in arr]
        count = 0
        for j in arr2:
            if j == ' ':
                count += 1
        if count == len(arr2):
            countN += 1
            if countN == 2:
                break
            equation += translate(arr_num)
            arr_num = []
        else:
            countN = 0
            arr_num.append(arr2)
    ans = eval(equation)
    print(equation)
    print(ans)
    r.sendlineafter('>>> ',str(ans))