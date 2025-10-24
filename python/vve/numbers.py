from __future__ import annotations

import re
import vim

import vve.visual
from vve import VveException


def to_hex(string: str) -> str:
    '''
    Takes an integer value as a string and converts it in the corresponding
    hex format. The returned hex string is always padded with '0x' and is
    aligned to a multiple of two bytes.

    Parameters:
        string              Integer value as string.

    Returns:
        number              Hex representation of input.
    '''
    try:
        number = hex(to_number(string))

    except ValueError:
        raise VveException(f"Specified string '{string}' is not an integer number.")

    if len(number) % 2:
        number = '0x0' + number[2:]

    return number


def to_bin(string: str) -> str:
    '''
    Takes an integer value as a string and converts it in the corresponding
    binary format. The returned binary string is always padded with '0b' and
    aligned to a multiple of eight bits.

    Parameters:
        string              Integer value as string.

    Returns:
        number              Binary representation of input.
    '''
    try:
        number = bin(to_number(string))[2:]

    except ValueError:
        raise VveException(f"Specified string '{string}' is not an integer number.")

    padding = (8 - len(number) % 8) % 8
    return '0b' + '0' * padding + number


def to_oct(string: str) -> str:
    '''
    Takes an integer value as a string and converts it in the corresponding
    octal format. The returned octal string is always padded with '0o'

    Parameters:
        string              Integer value as string.

    Returns:
        number              Octal representation of input.
    '''
    try:
        return oct(to_number(string))

    except ValueError:
        raise VveException(f"Specified string '{string}' is not an integer number.")


def to_dec(string: str) -> str:
    '''
    Takes an integer value as a string and converts it in the corresponding
    decimal format.

    Parameters:
        string              Integer value as string.

    Returns:
        number              Decimal representation of input.
    '''
    try:
        return str(to_number(string))

    except ValueError:
        raise VveException(f"Specified string '{string}' is not an integer number.")


def to_hex_string(string: str) -> str:
    '''
    Takes an integer value as a string and converts it in the corresponding
    hex-string format. Each byte of the returned hexstring is prefixed with
    '\\x' and the hexstring is aligned to two bytes.

    Parameters:
        string              Integer value as string.

    Returns:
        number              Hex representation of input.
    '''
    number = to_hex(string)[2:]
    hexList = [number[i:i+2] for i in range(0, len(number), 2)]

    return '\\x' + '\\x'.join(hexList)


def to_number(string: str) -> str:
    '''
    Takes a string that reprsents a number and converts it to a python number.
    Hexstrings are also allowed

    Parameters:
        string              String that represents a number.

    Returns:
        number              Hexnumber representation of input.
    '''
    if '\\' in string:
        number = '0x' + re.sub('\\\\x', '', string)
        return int(number, 16)

    return int(string, 0)


def _remember_format(string: str) -> str:
    '''
    Small helper function which determines the input format of a number representing
    string and returns the corresponding converter function for the back transformation.

    Parameters:
        string              String that represents a number.

    Returns:
        function            Function that transforms into this format
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
        raise VveException(f"Specified string '{string}' is not an integer number.")


def _get_number(prompt: str) -> int:
    '''
    Helper function that asks the user for a number. The specified input parameter is
    used for the prompt.

    Parameters:
        prompt              Prompt that is displayed within the dialog.

    Returns:
        number              Number that was entered by the user.
    '''
    user_input = vim.eval(prompt)

    try:
        return int(user_input, 0)

    except ValueError:
        raise VveException(f"Specified string '{user_input}' is not an integer number.")


def add(number1: str) -> str:
    '''
    Takes the string representation of a number and asks the user for a second
    number to add, adds the two numbers and returns the result.

    Parameters:
        string              String that represents a number.

    Returns:
        result              Result of the addition.
    '''
    restore_format = _remember_format(number1)
    result = int(number1, 0) + _get_number("input('Number to add: ')")

    return restore_format(str(result))


def sub(number1: str) -> str:
    '''
    Takes the string representation of a number and asks the user for a second
    number to subtract, subtracts the two numbers and returns the result.

    Parameters:
        string              String that represents a number.

    Returns:
        result              Result of the subtraction.
    '''
    restore_format = _remember_format(number1)
    result = int(number1, 0) - _get_number("input('Number to subtract with: ')")
    return restore_format(str(result))


def mul(number1: str) -> str:
    '''
    Takes the string representation of a number and asks the user for a second
    number to multiply, multiplies the two numbers and returns the result.

    Parameters:
        string              String that represents a number.

    Returns:
        result              Result of the multiplication.
    '''
    restore_format = _remember_format(number1)
    result = int(number1, 0) * _get_number("input('Number to multiply with: ')")
    return restore_format(str(result))


def div(number1: str) -> str:
    '''
    Takes the string representation of a number and asks the user for a second
    number to divide with, divides the two numbers and returns the result.

    Parameters:
        string              String that represents a number.

    Returns:
        result              Result of the dividation.
    '''
    restore_format = _remember_format(number1)

    try:
        result = int(number1, 0) // _get_number("input('Number to divide with: ')")

    except ZeroDivisionError:
        raise VveException('Division with zero is not possible.')

    return restore_format(str(result))


local_functions = locals()


def numbers_apply(function_name: str, visualmode: str) -> None:
    '''
    Just a helper function that applies {function_name} to the last
    visual selection. The last visual selection is then replaced by
    the corresponding result.

    Parameters:
        function_name       Name of the function to apply
        visualmode          Mode of last visual selection (v|V|^V).

    Returns:
        None
    '''
    funcref = local_functions[function_name]
    vve.visual.visual_apply(funcref, visualmode)
