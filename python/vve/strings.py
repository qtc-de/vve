from __future__ import annotations

import re
import vim

import vve.visual
from vve import VveException


def _make_upper(match: re.Match) -> str:
    '''
    Helper function that converts the first match group of a regex
    search to uppercase.

    Parameters:
        match           regex match

    Return:
        first match group in uppercase
    '''
    return match.group(1).upper()


def _get_hex_format(hs: str) -> str:
    '''
    Checks wether a supplied hex-string is a plain hexstring or a
    string with ' \\x..' encoding.

    Parameters:
        hs              hex string to check

    Returns
        return          plain | formatted | None
    '''
    if re.match('^0x([a-fA-F0-9]{2})+$', hs):
        return 'number'

    if re.match('^([a-fA-F0-9]{2})+$', hs):
        return 'plain'

    if re.match('^(\\\\x[a-fA-F0-9]{2})+$', hs):
        return 'formatted'

    return None


def string_length(string: str) -> None:
    '''
    Simply echos the length of the input string.

    Parameters:
        string          input string

    Returns:
        None
    '''
    vim.command('redraw')
    print(len(string))


def line_count(string: str) -> None:
    '''
    Takes a multiline string and echos the number of lines.

    Parameters:
        string          input string

    Returns:
        None
    '''
    vim.command('redraw')
    split = string.split('\n')

    if split[-1] == '':
        split = split[0:-1]

    print(len(split))


def string_length_hex(string: str) -> None:
    '''
    A length function for hex inputs (plain 0x.. and \\x.. format).

    Parameters:
        string          input string

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


def string_upper(string: str) -> str:
    '''
    Simply converts the input string to uppercase

    Parameters:
        string          input string

    Returns:
        string          input string in uppercase
    '''
    return string.upper()


def string_lower(string: str) -> str:
    '''
    Simply converts the input string to lowercase

    Parameters:
        string          input string

    Returns:
        string          input string in lowercase
    '''
    return string.lower()


def swap_endian_hs(hs: str) -> str:
    '''
    Takes a hexstring (\\x..\\x..\\x.. ...) and simply returns it in
    reverse order (swapped endian).

    Parameters:
        hs          hex string in '\\x..' format

    Returns:
        hs          hex string with swapped endian
    '''
    hexList = [hs[i:i+4] for i in range(0, len(hs), 4)]
    hexList.reverse()

    return ''.join(hexList)


def swap_endian_plain(hs: str) -> str:
    '''
    Takes a hexstring (without 0x or \\x) and simply returns it in
    reverse order (swapped endian).

    Parameters:
        hs          hex string in plain format

    Returns:
        hs          hex string with swapped endian
    '''
    hexList = [hs[i:i+2] for i in range(0, len(hs), 2)]
    hexList.reverse()

    return ''.join(hexList)


def swap_endian(hs: str) -> str:
    '''
    Checks the encoding of the supplied hexstring and calls the according endian
    swap function.

    Parameters:
        hs              hex string

    Returns:
        hs              hex string with swapped endianess
    '''
    hex_format = _get_hex_format(hs)

    if hex_format == 'number':
        return '0x' + swap_endian_plain(hs[2:])

    if hex_format == 'plain':
        return swap_endian_plain(hs)

    if hex_format == 'formatted':
        return swap_endian_hs(hs)

    return hs


def string_markdown_anchor(headline: str) -> str:
    '''
    Takes a string that represents a markdown headline and returns the
    corresponding anchor string.

    Parameters:
        headline        markdown headline

    Returns:
        anchor          corresponding anchor string
    '''
    headline = headline.lower()
    headline = headline.replace(' ', '-')

    return '#' + headline


def string_markdown_anchor_reference(headline: str) -> str:
    '''
    Takes a string that represents a markdown headline and returns a
    corresponding reference (link) to the anchor.

    Parameters:
        headline        markdown headline

    Returns:
        reference       anchor reference
    '''
    reference = f'[{headline}]('
    headline = string_markdown_anchor(headline)

    return reference + headline + ')'


def string_snake_case(string: str) -> str:
    '''
    Takes an input string in CamelCase format and converts it to snake case.

    Parameters:
        string          input string in camel case

    Returns:
        output          output string in snake case
    '''
    output = re.sub(r'(?<!^)([A-Z])', r'_\1', string)
    return output.lower()


def string_camel_case(string: str) -> str:
    '''
    Takes an input string in snake_case format and converts it to camelCase.

    Parameters:
        string          input string in snake case

    Returns:
        output          output string in camel case
    '''
    output = re.sub(r'_([^_])', _make_upper, string)
    return output


def string_reverse(string: str) -> str:
    '''
    Output reverse version of the input string.

    Parameters:
        string          input string in snake case

    Returns:
        output          output string in camel case
    '''
    return string[::-1]


local_functions = locals()


def strings_apply(function_name: str, visualmode: str) -> None:
    '''
    Just a helper function that applies {function_name} to the last
    visual selection. The last visual selection is then replaced by
    the corresponding result.

    Parameters:
        function_name           Name of the function to apply
        visualmode              Mode of last visual selection (v|V|^V).

    Returns:
        None
    '''
    funcref = local_functions[function_name]
    vve.visual.visual_apply(funcref, visualmode)


def strings_invoke(function_name: str) -> None:
    '''
    Just a helper function that applies {function_name} to the last
    visual selection. Instead of replacing the last visual selection
    with the result, no further actions are taken. {function_name} is
    expected to produce a meaningfull result (like echoing a message
    to the user).

    Parameters:
        function_name           Name of the function to apply

    Returns:
        None
    '''
    funcref = local_functions[function_name]
    selection = vve.visual.visual_select()

    try:
        funcref(selection)

    except VveException as e:

        vim.command('redraw')
        print('[Error] - ' + str(e))

        return
