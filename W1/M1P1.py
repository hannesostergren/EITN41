##Convert data & luhns algorithm
import math
import hashlib

# def int_to_byte(n):
#     byte = ""
#     k = 0
#     while (2**k < n):
#         k += 1
#     if(n / 2**k == 1):
#         byte = byte + "1"
#     while (k > 0):
#         res = math.floor(n / 2) 
#         rem = n % 2
#         byte = byte + str(rem)
#         n = res
#         k -= 1
#     return byte

# def int_to_hex(n):
#     byte = ""
#     k = 0
#     let = ['a', 'b', 'c', 'd', 'e', 'f']
#     while(16**k < n):
#         k += 1
#     if(n / 16**k == 1):
#         byte = byte + "1"
#     while (k > 0):
#         res = math.floor(n/16)
#         rem = n % 16
#         if(rem >= 10):
#             byte = byte + str(let[rem-10])
#         else:
#             byte = byte + str(rem)
#         n = res
#         k -= 1
#     byte = byte[::-1]
#     return byte

# def byte_to_int(n):
#     intN = 0
#     for k, i in enumerate(str(n)[::-1]):
#         intN += 2**k * int(i)
#     return intN
# def byte_to_hex(n):
#     return int_to_hex(byte_to_int(n))
# def hex_to_int(n):
#     let = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f']
#     intN = 0
#     for k, i in enumerate(str(n)[::-1]):
#         intN += 16**k * let.index(i)
#     return intN
# def hex_to_byte(n):
#     return int_to_byte(hex_to_int(n))


##Convert data & luhns algorithm
import math
import hashlib

def int_to_byte(n, leng, order):
    return n.to_bytes(leng, order)

def int_to_hex(n):
    return hex(n)

def byte_to_int(n):
    return int.from_bytes(n, 'big')
def byte_to_hex(n):
    return n.hex()
def hex_to_int(n):
    return int(n, 16)
def hex_to_byte(n):
    return bytes.fromhex(str(n))


def luhn(cardNumber):
    x_idx = cardNumber[::-1].index("X")
    cardNumber = cardNumber.replace("X", "0")
    possible_x = (10 - sum(double_even(cardNumber))) % 10
    if x_idx % 2 == 0: #index of x
        return possible_x
    elif possible_x % 2 == 0: #even x, therefore doubled
        return int(possible_x / 2)
    else:
        return int((possible_x + 9) / 2) #else return next possible x mod 2

def double_even(s):
    new_num = []
    for i, n in enumerate(s[::-1]):
        even = i % 2 == 1
        if even:
            num = int(n) * 2
            if num >= 10:
                num = num - 9
            new_num.append(num)
        else: 
            new_num.append(int(n))
    return new_num

if __name__ == "__main__":
    with open("quiz_input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            print(int(luhn(line)), end="")
    print("")
    print(byte_to_int(hex_to_byte("22decaf000c0ffee")))
    print(hashlib.sha256(int_to_byte(3119, 4, "big")).hexdigest())

#37b57c5f4fc4fb0f53aee3a086c91fe0ecbca0ec4973261c7f54b36c038c2711