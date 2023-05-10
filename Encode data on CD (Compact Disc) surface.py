"""
"Pits" and "lands" are physical features on the surface of a CD that represent binary data. Pits are small depressions or grooves on the surface of the CD, while lands are flat areas between two adjacent pits.

The pits and lands themselves do not directly represent the zeros and ones of binary data. Instead, Non-return-to-zero, inverted encoding is used: a change from pit to land or land to pit indicates a one, while no change indicates a zero.

In this Kata, you should implement a function, that takes integer in range [0..255] (8 bits), and returns combination of pits and lands that encode the number. Result should have format of string: PLLPL... where P represents pit and L represents land. Combination should always start with pit. Numbers should be encoded in little-endian, which means you start from least significant bit.

Example
Input: 5

Binary representation (8 bits): 00000101

Output: PLLPPPPPP

Explanation:

Starts from P as per description
Changes to L because first bit is 1
Stays L because second bit is 0
Changes to P because third bit is 1
Stays P because fourth bit is 0
Stays P till the end because all subsequent bits are 0
"""


def code_CD(number):
    if number > 255:
        return -1
    forma = format(number, '08b')
    form = forma[::-1]
    res = "P"
    p = 'P'
    l = 'L'
    for f in form:
        if f == '1':  # 1 it is always change letter to another letter
            p, l = l, p
        res += p
    return res


# PL = 1 or 11,   #

print(code_CD(5))
print(code_CD(5), "PLLPPPPPP", 'Failed on number 5')  # 5 = 00000101
print(code_CD(16), "PPPPPLLLL", 'Failed on number 16')  # 16 = 00010000
print(code_CD(63), "PLPLPLPPP", 'Failed on number 63')  # 63 = 00111111
print(code_CD(222), "PPLPLPPLP", 'Failed on number 222')  # 222 = 11011110


print('**********')
encode_cd=lambda n,x=0:'P'+''.join('PL'[x:=x^int(b)]for b in f'{n:08b}'[::-1])
print('**********')
from itertools import accumulate

def encode_cd2(n):
    return ''.join(accumulate(
        map(int, reversed(f'{ n :0>8b}')),
        lambda pit,b: pit if not b else 'PL'[pit=='P'],
        initial='P'
    ))
print('**********')
def encode_cd3(n):
    res = 'P'
    for b in f'{n:08b}'[::-1]:
        res += 'PLP'[(res[-1]=='P') + (b=='0')]
    return res
print('**********')
def encode_cd4(n):
    FEATURES = ['P', 'L']
    state = 0
    result = FEATURES[state]
    for _ in range(8):
        if n % 2 == 1:
            state = (state + 1) % 2
        n //= 2
        result += FEATURES[state]
    return result
print('**********')
from itertools import accumulate
from operator import xor

def encode_cd5(n):
    bits = map(int, reversed(f'{n:08b}'))
    return ''.join(map('LP'.__getitem__, accumulate(bits, xor, initial=1)))
print('**********')
def encode_cd6(n):
    en = bin(n)[2:].rjust(8, '0')[::-1]
    res = "P"
    for i in en:
        if i == '0':
            res+=res[-1]
        elif res[-1] == 'P':
            res+='L'
        else:
            res+='P'
    return res
print('**********')
def encode_cd7(n):
    n = bin(n)[2:].rjust(8, '0')[::-1]
    output = 'P'
    cur = 0
    for i in n:
        if i == '1':
            cur ^= 1
        output += 'PL'[cur]
    return output
print('**********')

from re import sub
from itertools import cycle

def encode_cd8(n):
    c=cycle('PL')
    if n&1: next(c)
    return 'P'+sub(r'10*|0+',lambda m:(next(c)or m[0][0]>'0'and next(c))*len(m[0]),'{:08b}'.format(n)[::-1])
print('**********')
def encode_cd9(n):
    result = 'P'
    for x in f'{n:b}'.zfill(8)[::-1]:
        result += result[-1] if x == '0' else 'L' if result[-1] == 'P' else 'P'
    return result
print('***********')
def encode_cd10(n):
    s = "P"
    for _ in range(8):
        s += "PL"[n + (s[-1] == "L") & 1]
        n >>= 1
    return s


def encode_cd100(n):
    # Here's an another artical
    binary_n = bin(n)
    binary_n = binary_n[2:]
    result = "P"
    if len(binary_n) < 8:
        for i in range(8 - len(binary_n)):
            binary_n = "0" + binary_n
    binary_n = binary_n[::-1]

    for i in range(8):
        if binary_n[i] == "0":
            result += result[i]
        elif binary_n[i] == "1":
            if result[i] == "P":
                result += "L"
            else:
                result += "P"

    return result