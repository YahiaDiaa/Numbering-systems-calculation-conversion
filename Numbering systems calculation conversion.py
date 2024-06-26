# 6 functions ahead 3 of them are to convert decimal to the all numbers and the others are from all numbers to decimal
def binary_to_decimal(bn):  # the first one from binary to decimal
    bn = globals()['binary']
    bn = int(bn)
    dec, i = 0, 0
    while bn > 0:
        r = bn % 2
        exp = r * (2 ** i)
        dec = dec + exp
        bn = bn // 10
        i += 1
    return dec


def octal_to_decimal(octal):  # the second is from octal to decimal
    # octal = globals()['octal']
    dec_val = 0
    i = 0
    while int(octal) > 0:
        r = int(octal) % 10
        dec_val = dec_val + r * (8 ** i)
        octal = int(octal) // 10
        i += 1
    return dec_val


def decimal_to_octal(decimal):  # the third from decimal to octal
    decimal = globals()['decimal']
    octal = []
    while decimal > 0:
        octal.insert(0, decimal % 8)
        decimal = decimal // 8
    for i in range(0, len(octal)):
        print(octal[i], end="")


counter = 1
counter2 = 1
counter3 = 1


def binary_to_decimal(bn):  # the 4th is from binary to decimal
    # bn = globals()['binary']
    bn = int(bn)
    dec, i = 0, 0
    while bn > 0:
        r = bn % 2
        exp = r * (2 ** i)
        dec = dec + exp
        bn = bn // 10
        i += 1

    return dec


def splitnum(x):  # these two functions are from decimal to hexadecimal
    truenum = int(x)
    dicemal = x - truenum
    return truenum, dicemal


def decimal_to_hexadecimal(bn):
    # num = globals()['decimal']
    resultCach = {}

    finalResultInt = ""
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '16', '9', "A", 'B', 'C', 'D', 'E', 'F']
    bn, dec1 = splitnum(bn)

    reminder = bn / 16
    while (reminder > 0):
        num, dec = splitnum(reminder)
        finalResultInt += hex[int(dec * 16)]
        reminder = num / 16

    finalResultInt = finalResultInt[::-1]
    # print(finalResultInt)

    finalResultDec = ""
    result = dec1 * 16
    # print(result)
    resultCach[dec1] = True
    while (result > 0):
        num, dec = splitnum(result)
        resultCach[dec1] = True
        if (num in resultCach):
            break
        finalResultDec += hex[int(num)]
        result = dec * 16
    # print(finalResultDec)
    print(finalResultInt)


def hexa_to_decimal(num):  # this one is from hexadecimal to decimal
    dec = {"0": 0,
           "1": 1,
           "2": 2,
           "3": 3,
           "4": 4,
           "5": 5,
           "6": 6,
           "7": 7,
           "8": 8,
           "9": 9,
           "A": 10,
           "B": 11,
           "C": 12,
           "D": 13,
           "E": 14,
           "F": 15,
           }
    sum = 0
    string = str(num)
    length = len(num)  # lanth of num starting from 1
    for i in range(length):  # i start from zero
        sum += (dec[string[length - i - 1].upper()] * 16 ** (i))
    return sum


def decimal_to_binary():  # this is from decimal to binary
    binary = []
    dec = globals()['decimal']
    while dec != 0:
        binary.insert(0, dec % 2)
        dec = dec // 2
    for i in range(0, len(binary)):
        print(binary[i], end="")


def decimal_to_octal():
    decimal = globals()['decimal']
    octal = []
    while decimal > 0:
        octal.insert(0, decimal % 8)
        decimal = decimal // 8
    for i in range(0, len(octal)):
        print(octal[i], end="")


def octal_to_decimal(octal):
    # octal = globals()['octal']
    dec_val = 0
    i = 0
    while int(octal) > 0:
        r = int(octal) % 10
        dec_val = dec_val + r * (8 ** i)
        octal = int(octal) // 10
        i += 1

    return dec_val


#####################################################################################################################################################################################
# MAIN PROGRAM
#####################################################################################################################################################################################
# IF THE USER WANTS TO CONVERT FROM DECIMAL TO ANY NUMBER WE ALREADY HAVE DONE THIS FUNCTION ALL WE NEED IS TO CALL IT
# BUT FIRST WE NEED TO CHECK WHAT KIND OF NUMBER THE USER WANTS TO INPUT
# IF THE USER WNATS TO CINVERT ANY NUMBER TO ANOTHER ONE EXCEPT DECIMAL (LIKE FROM BINARY TO OCTAL ) WE JUST NEED TO CONVERT THE FIRST NUMBER TO DECIMAL AND
# THEN CONVERT THE DECIMAL
# SO WE NEED TO RETURN VALUE FROM ALL FUNCTIONS THAT CONVERT (ANY NUMBER) TO DECIMAL LIKE WHAT WE DID IN THE PREVIOUS FUNCTIONS
# BUT THE OTHER FUNCTION (FROM DECIMAL TO ANY NUMBER) WE JUST NEED TO PRINT IT AUTOMATICALLY
while counter > 0:
    # We made a while loop to check the user input if he choose 'A' that's mean he wants to insert a number, 'B' it means he wants to exit the programm
    # if he chooses anything else he will return to here again
    choice = input(""" 
Please choose an option
 A) insert a number 
 B) exit the program \n""")
    if choice.upper() == 'A':  # we checked if the user choosed to insert a number
        # we will ask him what kind of number do you want to insert
        while counter2 > 0:  # we made another loop to check if he chooses an invalid choice like 'E' for example
            # the loop will be break and then he will return to the first quesrtion which is in the code number '161'
            user_choice = input("""
      What kind of number you want to write    
          A)Decimal                                       
          B)Binary 
          C)Hexadecimal
          D)octal
          \n""")
            istrue = 0
            while user_choice.upper() == 'A':  # if he chooses to insert a decimal number

                decimal = input("Enter a decimal number \n")  # we made an inout for this

                while decimal:  # and then we made a loop for this decimal to know the convert will be to what number

                    user_choice_decimal_to = input("""
                  transfer your number into :
                 A) binary
                 b) hexadecimal
                 c) octal \n""")
                    if user_choice_decimal_to.upper() == 'A':  # this if condition is to check every choice, valid and invalid one
                        decimal = int(decimal)  # we made the decimal input an integer to make the process on it
                        decimal_to_binary()  # we call the function that convert from decimal to binary
                        break  # we break everything to know if he wants to insert a number again or exit the programm

                    elif user_choice_decimal_to.upper() == 'B':  # the same thing that happen in the last check
                        decimal = int(decimal)
                        decimal_to_hexadecimal(decimal)
                    elif user_choice_decimal_to.upper() == 'C':
                        decimal = int(decimal)
                        decimal_to_octal()
                        break
                    else:
                        print("invalid choice")  # this else is for the invalid choices

                    break
                break

            while user_choice.upper() == 'B':  # this loop will work if he choosed to insert a binary number

                binary = input("Enter a binary number \n")

                while binary:  # the same while loop to check valid and invalid choices
                    convertion_2 = input("""
                 transfer your number into :
                A) decimal
                b) hexadecimal
                c) octal \n""")
                    if convertion_2.upper() == 'A':
                        print(binary_to_decimal(binary))
                        break
                    elif convertion_2.upper() == 'B':  # here when he choose to convert from binary to hexadecimal
                        decimal_result = binary_to_decimal(
                            binary)  # we convert the binary first to a decimal and saved the value in this variable called (decimal_result)
                        decimal_to_hexadecimal(
                            decimal_result)  # then we called the function that convert decimal to hexadecima and used the variable(decimal_result) instead of the parametere

                    elif convertion_2.upper() == 'C':  # the same as the last one
                        decimal = binary_to_decimal(binary)
                        # decimal_to_octal(decimal)
                        decimal_to_octal()
                    else:
                        print("Invalid choice")
                    break
                break
            break

            # break

            # we will do the same things at the rest of the code
        while user_choice.upper() == 'C':

            hexadecimal = input("Enter a hexadecimal number \n")

            while hexadecimal:
                user_choice = convertion3 = input("""
                 transfer your number into :
                A) binary
                b) decimal
                c) octal \n""")
                if user_choice.upper() == 'A':
                    decimal = hexa_to_decimal(hexadecimal)
                    decimal_to_binary()
                    break
                elif user_choice.upper() == 'B':
                    print(hexa_to_decimal(hexadecimal))
                    break
                elif user_choice.upper() == 'C':
                    decimal = hexa_to_decimal(hexadecimal)
                    decimal_to_octal()
                    break
                else:
                    print("Invalid choice")
                    break
            break
        while user_choice.upper() == 'D':

            octal = input("Enter octal number \n")

            while octal:
                convertion4 = input("""
                 transfer your number into :
                A) binary
                b) hexadecimal
                c) decimal \n""")
                if convertion4.upper() == 'A':
                    decimal = octal_to_decimal(octal)
                    decimal_to_binary()
                    break
                elif convertion4.upper() == 'B':
                    decimal = octal_to_decimal(octal)
                    decimal_to_hexadecimal(decimal)
                    break
                elif convertion4.upper() == 'C':
                    print(octal_to_decimal(octal))
                    break
            break








    elif choice.upper() == 'B':
        print("thanks for using my program")
        break
    else:
        print("please choose valid choice \n")

counter += 1

""" 
NAME:                                            ID:
Yahia Diaa Eldin Mohamed Nagiub                  20230470
Ahmed Ashraf Mohamed Bedir Ahmed                 20230006
Moaz Yasser Mahmoud Ali                          20230411
"""