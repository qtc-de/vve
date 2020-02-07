import re
import html
import base64
import binascii
import urllib.parse
import xml.sax.saxutils 

import vve.visual


def encode_base64(string):
    '''
    Applies base64 encoding to the input string.

    Parameters:
        string              (string)            Input string

    Returns:
        encoded             (string)            Base64 encoded output
    '''
    global encode_return
    byte_form = string.encode('utf-8')
    encoded = base64.b64encode(byte_form)
    return encoded.decode('utf-8')


def decode_base64(string):
    '''
    Takes a base64 input string and returns the decoded data. Padding
    errors are corrected automatically (theoretically).

    Parameters:
        string              (string)            Input string

    Returns:
        decoded             (string)            Base64 decoded data
    '''
    byte_form = string.encode('utf-8')
    count = 0

    while count < 3:
        try:
            decoded = base64.b64decode(byte_form)
            decoded = decoded.decode('utf-8')
            break

        except binascii.Error:
            byte_form += b'='
            decoded = string
            count += 1
            continue

        except:
            print("[-] Input cannot be decoded")
            decoded = string
            break

    return decoded


def encode_binary(string):
    '''
    Applies binary encoding to the input string. Each character is
    interpreted as an utf-8 encoded byte sequence and is translated
    into a eight digit binary sequence.

    Parameters:
        string              (string)            Input string

    Returns:
        return_value        (string)            Binary formatted output
    '''
    byte_form = string.encode('utf-8')
    return_value = ''
    for byte in byte_form:
        binary = "{:08b}".format(byte)
        return_value += binary
    return return_value


def decode_binary(string):
    '''
    Takes a binary formatted string (containing only zeros and ones)
    and tries to decode it as an utf-8 formatted string.

    Parameters:
        string              (string)            Input binary string

    Returns:
        string              (string)            utf-8 decoded output
    '''
    if re.search('[^01]', string):
        print("[-] Binary input string expected!")
        return string
    b_array = bytearray()
    for i in range(0, len(string), 8):
        integer = int(string[i:i+8], 2)
        b_array.append(integer)
    try:
        return b_array.decode('utf-8')
    except:
        print("[-] Input cannot be decoded as 'utf-8'.")
        return string


def encode_hex_string(string):
    '''
    Takes an utf-8 formatted string and converts it into a hex-string
    (\\x..\\x..\\x..). 

    Parameters:
        string              (string)            Input string

    Returns:
        return_value        (string)            Formatted hex output
    '''
    byte_form = string.encode('utf-8')
    hex_form = byte_form.hex()
    return_value = ''
    for i in range(0, len(hex_form), 2):
        return_value += '\\x' + hex_form[i:i+2]
    return return_value


def decode_hex_string(string):
    '''
    Takes a hex string (\\x..\\x..\\x..) as input and converts it back into
    an utf-8 formatted string.

    Parameters:
        string              (string)            Input hex string

    Returns:
        string              (string)            UTF-8 formatted output
    '''
    plain = string.replace('\\x', '')
    try:
        b_array = bytearray.fromhex(plain)
    except:
        print("[-] Hex input string expected!")
        return string
    try: 
        return b_array.decode('utf-8')
    except:
        print("[-] Input cannot be decoded as 'utf-8'.")
        return string
        

def encode_hex(string):
    '''
    Takes a string as input and converts it into a stream of hex numbers.
    The input string is utf-8 decoded first and then each byte will be converted
    into a hex number. The single hex numbers will then be concatenated.

    Parameters:
        string              (string)            Input string

    Returns:
        string              (string)            Hex formatted output
    '''
    byte_form = string.encode('utf-8')
    return byte_form.hex()


def decode_hex(string):
    '''
    Takes a stream of hex numbers (e.g. A01FE92...) and converts it into a
    utf-8 formatted string.

    Parameters:
        string              (string)            Input hex stream

    Returns:
        string              (string)            UTF-8 formatted output
    '''
    try: 
        b_array = bytearray.fromhex(string)
    except:
        print("[-] Hex input string expected!")
        return string
    try: 
        return b_array.decode('utf-8')
    except:
        print("[-] Input cannot be decoded as 'utf-8'.")
        return string


def encode_url_full(string):
    '''
    Takes a string as input and applies URL encoding to each character.
    The input string is treated as utf-8 and multibyte characters are
    encoded as seperate URL encoded characters.

    Parameters:
        string              (string)            Input string

    Returns:
        string              (string)            URL encoded output
    '''
    byte_form = string.encode('utf-8')
    hex_form = byte_form.hex()
    return_value = ''
    for i in range(0, len(hex_form), 2):
        return_value += '%' + hex_form[i:i+2]
    return return_value


def encode_url(string):
    '''
    Applies URL encoding to the input string for URL special characters.

    Parameters:
        string              (string)            Input string

    Returns:
        string              (string)            URL encoded output
    '''
    return urllib.parse.quote_plus(string)


def decode_url(string):
    '''
    Applies URL decoding to the input string.

    Parameters:
        string              (string)            Input string

    Returns:
        string              (string)            URL decoded output
    '''
    return urllib.parse.unquote_plus(string)


def encode_xml(string):
    '''
    Applies XML encoding to the input string for XML special characters.

    Parameters:
        string              (string)            Input string

    Returns:
        string              (string)            XML encoded output
    '''
    return xml.sax.saxutils.escape(string)


def decode_xml(string):
    '''
    Applies XML decoding to the input string.

    Parameters:
        string              (string)            Input string

    Returns:
        string              (string)            XML decoded output
    '''
    return xml.sax.saxutils.unescape(string)


def encode_html_full(string):
    '''
    Applies HTML encoding to the complete input string. The input string
    is treated as utf-8 and each byte gets encoded seperately.

    Parameters:
        string              (string)            Input string

    Returns:
        string              (string)            HTML encoded output
    '''
    byte_form = string.encode('utf-8')
    hex_form = byte_form.hex()
    return_value = ''
    for i in range(0, len(hex_form), 2):
        return_value += '&#x' + hex_form[i:i+2] + ';'
    return return_value


def encode_html(string):
    '''
    Applies HTML encoding to special characrers inside the input string.

    Parameters:
        string              (string)            Input string

    Returns:
        string              (string)            HTML encoded output
    '''
    return html.escape(string)


def decode_html(string):
    '''
    Applies HTML decoding to the input string.

    Parameters:
        string              (string)            Input string

    Returns:
        string              (string)            HTML decoded output
    '''
    return html.unescape(string)


local_functions = locals()
def encode_apply(function_name, visualmode):
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
