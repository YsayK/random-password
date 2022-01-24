from random import sample
from pyperclip import copy

def do():
    lower_let = "abcdefghijklmnopqrstuvwxyz"
    upper_let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "?!@#$&()*/|\\"

    max_let = 30

    all = lower_let + lower_let + numbers + symbols

    try:
        length = int(input("\n\npassword length? : "))
    except:
        print("\nError: you didn't put the integer")
        do()
    else:
        if (0 < length <= max_let):
            password = "".join(sample(all, length))

            print("\n" + password)
            copy(password)
            print("\n(copied to copied to clipboard)")
            do()
        else:
            print("\nmaximum amount of characters is : " + str(max_let))
            do()

do()
