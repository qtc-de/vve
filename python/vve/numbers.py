import re
import vim

import vve.visual


def to_hex(string):
    '''
    Takes an integer value as a string and converts it in the corresponding
    hex format. The returned hex string is always padded with '0x' and is
    aligned to a multiple of two bytes.

    Parameters:
        string              (string)            Integer value as string.

    Returns:
        number              (string)            Hex representation of input.
    '''
    try:
        number = hex(int(string, 0))
    except ValueError:
        print(f"[-] Specified string '{string}' is not a number.")
        return string

    if len(number) % 2:
        number = "0x0" + number[2:]
    return number


def to_bin(string):
    '''
    Takes an integer value as a string and converts it in the corresponding
    binary format. The returned binary string is always padded with '0b' and
    aligned to a multiple of eight bits.

    Parameters:
        string              (string)            Integer value as string.

    Returns:
        number              (string)            Binary representation of input.
    '''
    try:
        number = int(string, 0)
    except ValueError:
        print(f"[-] Specified string '{string}' is not a number.")
        return string
    number = bin(number)[2:]
    while len(number) % 8:
        number = "0" + number
    number = "0b" + number
    return number


def to_oct(string):
    '''
    Takes an integer value as a string and converts it in the corresponding
    octal format. The returned octal string is always padded with '0o'

    Parameters:
        string              (string)            Integer value as string.

    Returns:
        number              (string)            Octal representation of input.
    '''
    try:
        number = int(string, 0)
    except ValueError:
        print(f"[-] Specified string '{string}' is not a number.")
        return string
    return oct(number)


def to_dec(string):
    '''
    Takes an integer value as a string and converts it in the corresponding
    decimal format.

    Parameters:
        string              (string)            Integer value as string.

    Returns:
        number              (string)            Decimal representation of input.
    '''
    try:
        number = int(string, 0)
    except ValueError:
        print(f"[-] Specified string '{string}' is not a number.")
        return string

    return str(number)


def to_hex_string(string):
    '''
    Takes an integer value as a string and converts it in the corresponding
    hex-string format. Each byte of the returned hexstring is prefixed with
    '\\x' and the hexstring is aligned to two bytes.

    Parameters:
        string              (string)            Integer value as string.

    Returns:
        number              (string)            Hex representation of input.
    '''
    try:
        number = to_hex(string)[2:]
        hexList = [number[i:i+2] for i in range(0, len(number), 2)]
        returnValue = "\\x" + "\\x".join(hexList)
    except Exception as error:
        print("[-] to_hex_string - Unexpected Error")
        print("[-] Error message: {}".format(error))
        returnValue = string
    return returnValue


def from_hex_string(string):
    '''
    Takes a hex string and converts it back into a hex number.

    Parameters:
        string              (string)            Hexstring.

    Returns:
        number              (string)            Hexnumber representation of input.
    '''
    try:
        number = "0x" + re.sub('\\\\x', '', string.decode("utf-8"))
        int(number, 16)
        return_value = number
    except Exception as error:
        print("[-] from_hex_string - Unexpected Error")
        print("[-] Error message: {}".format(error))
        return_value = string
    return return_value


def remember_format(string):
    '''
    Small helper function which determines the input format of a number representing
    string and that returns the corresponding converter function for the back
    transformation.

    Parameters:
        string              (string)            String that represents a number.

    Returns:
        function            (function)          Function that transforms into this format
    '''
    try:
        int(string, 10)
        return to_dec
    except ValueError:
        pass
    try:
        int(string, 16)
        return to_hex
    except ValueError:
        pass
    try:
        int(string, 8)
        return to_oct
    except ValueError:
        pass
    try:
        int(string, 2)
        return to_bin
    except ValueError:
        print("[-] remeber_format - Unable to determine input format")


def add(number1):
    '''
    Takes the string representation of a number and asks the user for a second
    number to add, adds the two numbers and returns the result.

    Parameters:
        string              (string)            String that represents a number.

    Returns:
        result              (string)            Result of the addition.
    '''
    restore_format = remember_format(number1)
    number2 = vim.eval("input('Number to add: ')")
    result = int(number1, 0) + int(number2, 0)
    return restore_format(str(result))


def sub(number1):
    '''
    Takes the string representation of a number and asks the user for a second
    number to subtract, subtracts the two numbers and returns the result.

    Parameters:
        string              (string)            String that represents a number.

    Returns:
        result              (string)            Result of the subtraction.
    '''
    restore_format = remember_format(number1)
    number2 = vim.eval("input('Number to subtract with: ')")
    result = int(number1, 0) - int(number2, 0)
    return restore_format(str(result))


def mul(number1):
    '''
    Takes the string representation of a number and asks the user for a second
    number to multiply, multiplies the two numbers and returns the result.

    Parameters:
        string              (string)            String that represents a number.

    Returns:
        result              (string)            Result of the multiplication.
    '''
    restore_format = remember_format(number1)
    number2 = vim.eval("input('Number to multiply with: ')")
    result = int(number1, 0) * int(number2, 0)
    return restore_format(str(result))


def div(number1):
    '''
    Takes the string representation of a number and asks the user for a second
    number to divide with, divides the two numbers and returns the result.

    Parameters:
        string              (string)            String that represents a number.

    Returns:
        result              (string)            Result of the dividation.
    '''
    restore_format = remember_format(number1)
    number2 = vim.eval("input('Number to divide with: ')")
    result = int(int(number1, 0) / int(number2, 0))
    return restore_format(str(result))


local_functions = locals()


def numbers_apply(function_name, visualmode):
    '''
    Just a helper function that applies {function_name} to the last
    visual selection. The last visual selection is then replaced by
    the corresponding result.

    Parameters:
        function_name       (string)            Name of the function to apply
        visualmode          (string)            Mode of last visual selection (v|V|^V).

    Returns:
        None
    '''
    funcref = local_functions[function_name]
    vve.visual.visual_apply(funcref, visualmode)
