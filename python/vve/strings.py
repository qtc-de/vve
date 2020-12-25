import re
import vim

import vve.visual
from vve import VveException


def _make_upper(match):
    '''
    Helper function that converts the first match group of a regex
    search to uppercase.
    '''
    return match.group(1).upper()


def _get_hex_format(hs):
    '''
    Checks wether a supplied hex-string is a plain hexstring or a
    string with ' \\x..' encoding.

    Parameters:
        hs          (string)            hex string to check

    Returns
        return      (string)            plain | formatted | None
    '''
    if re.match('^0x([a-fA-F0-9]{2})+$', hs):
        return 'number'
    if re.match('^([a-fA-F0-9]{2})+$', hs):
        return 'plain'
    if re.match('^(\\\\x[a-fA-F0-9]{2})+$', hs):
        return 'formatted'
    return None


def string_length(string):
    '''
    Simply echos the length of the input string.

    Parameters:
        string          (string)        input string

    Returns:
        None
    '''
    vim.command('redraw')
    print(len(string))


def string_length_hex(string):
    '''
    A length function for hex inputs (plain 0x.. and \\x.. format).

    Parameters:
        string          (string)        input string

    Returns:
        None
    '''
    hex_format = _get_hex_format(string)

    if hex_format == 'number':
        length = len(string) // 2 - 1

    elif hex_format == 'plain':
        length = len(string) // 2

    elif hex_format == 'formatted':
        length = len(string) // 4

    else:
        raise VveException(f"Input string '{string}' is not in hex format.")

    vim.command('redraw')
    print(length)


def string_upper(string):
    '''
    Simply converts the input string to uppercase

    Parameters:
        string          (string)        input string

    Returns:
        string          (string)        input string in uppercase
    '''
    return string.upper()


def string_lower(string):
    '''
    Simply converts the input string to lowercase

    Parameters:
        string          (string)        input string

    Returns:
        string          (string)        input string in lowercase
    '''
    return string.lower()


def swap_endian_hs(hs):
    '''
    Takes a hexstring (\\x..\\x..\\x.. ...) and simply returns it in
    reverse order (swapped endian).

    Parameters:
        hs          (string)            hex string in '\\x..' format

    Returns:
        hs          (string)            hex string with swapped endian
    '''
    hexList = [hs[i:i+4] for i in range(0, len(hs), 4)]
    hexList.reverse()
    return "".join(hexList)


def swap_endian_plain(hs):
    '''
    Takes a hexstring (without 0x or \\x) and simply returns it in
    reverse order (swapped endian).

    Parameters:
        hs          (string)            hex string in plain format

    Returns:
        hs          (string)            hex string with swapped endian
    '''
    hexList = [hs[i:i+2] for i in range(0, len(hs), 2)]
    hexList.reverse()
    return "".join(hexList)


def swap_endian(hs):
    '''
    Checks the encoding of the supplied hexstring and calls the according endian
    swap function.

    Parameters:
        hs          (string)            hex string

    Returns:
        hs          (string)            hex string with swapped endianess
    '''
    hex_format = _get_hex_format(hs)
    if hex_format == 'number':
        return '0x' + swap_endian_plain(hs[2:])
    if hex_format == 'plain':
        return swap_endian_plain(hs)
    if hex_format == 'formatted':
        return swap_endian_hs(hs)
    return hs


def string_markdown_anchor(headline):
    '''
    Takes a string that represents a markdown headline and returns the
    corresponding anchor string.

    Parameters:
        headline    (string)            markdown headline

    Returns:
        anchor      (string)            corresponding anchor string
    '''
    headline = headline.lower()
    headline = headline.replace(" ", "-")
    anchor = "#" + headline
    return anchor


def string_markdown_anchor_reference(headline):
    '''
    Takes a string that represents a markdown headline and returns a
    corresponding reference (link) to the anchor.

    Parameters:
        headline    (string)            markdown headline

    Returns:
        reference   (string)            anchor reference
    '''
    reference = f'[{headline}]('
    headline = string_markdown_anchor(headline)
    reference += headline + ')'
    return reference


def string_snake_case(string):
    '''
    Takes an input string in CamelCase format and converts it to snake case.

    Parameters:
        string      (string)            input string in camel case

    Returns:
        output      (string)            output string in snake case
    '''
    output = re.sub(r'(?<!^)([A-Z])', r'_\1', string)
    return output.lower()


def string_camel_case(string):
    '''
    Takes an input string in snake_case format and converts it to camelCase.

    Parameters:
        string      (string)            input string in snake case

    Returns:
        output      (string)            output string in camel case
    '''
    output = re.sub(r'_([^_])', _make_upper, string)
    return output


local_functions = locals()


def strings_apply(function_name, visualmode):
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


def strings_invoke(function_name):
    '''
    Just a helper function that applies {function_name} to the last
    visual selection. Instead of replacing the last visual selection
    with the result, no further actions are taken. {function_name} is
    expected to produce a meaningfull result (like echoing a message
    to the user).

    Parameters:
        function_name       (string)            Name of the function to apply

    Returns:
        None
    '''
    funcref = local_functions[function_name]
    selection = vve.visual.visual_select()

    try:
        funcref(selection)

    except VveException as e:
        vim.command('redraw')
        print("[Error] - " + str(e))
        return
