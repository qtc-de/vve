import re
import html
import base64
import binascii
import urllib.parse
import xml.sax.saxutils 

import vve.visual
from vve import VveException


def encode_base64(data):
    '''
    Applies base64 encoding to the input data. Input can be supplied
    as string or bytes value.

    Parameters:
        data                (string/bytes)      Input data

    Returns:
        encoded             (string)            Base64 encoded output
    '''
    if not isinstance(data, bytes):
        data = data.encode('utf-8')

    encoded = base64.b64encode(data)
    return encoded.decode('utf-8')


def decode_base64(string, raw=False):
    '''
    Takes a base64 input string and returns the decoded data. Padding
    errors are corrected automatically (theoretically). Output can be
    obtained as string or bytes depending on the value of raw.

    Parameters:
        string              (string)            Input string
        raw                 (boolean)           Return as bytes

    Returns:
        decoded             (string/bytes)      Base64 decoded data
    '''
    byte_form = string.encode('utf-8')
    count = 0

    while count < 3:
        try:
            decoded = base64.b64decode(byte_form, validate=True)
            if raw:
                return decoded

            decoded = decoded.decode('utf-8')
            break

        except binascii.Error:
            byte_form += b'='
            decoded = string
            count += 1
            continue

        except:
            raise VveException("Decoded result cannot be encoded as UTF-8.")

    if count >= 3:
        raise VveException("Input is no valid base64.")

    return decoded


def encode_binary(data):
    '''
    Applies binary encoding to the input data. Input can be supplied
    as string or bytes. If it is string, each character is
    interpreted as an utf-8 encoded byte sequence and is translated
    into a eight digit binary sequence.

    Parameters:
        data                (string/bytes)      Input data

    Returns:
        return_value        (string)            Binary formatted output
    '''
    if not isinstance(data, bytes):
        data = data.encode('utf-8')

    return_value = ''
    for byte in data:
        binary = "{:08b}".format(byte)
        return_value += binary

    return return_value


def decode_binary(string, raw=False):
    '''
    Takes a binary formatted string (containing only zeros and ones)
    and tries to decode it as an utf-8 formatted string. Output can
    also be obtained as raw bytes if raw=True.

    Parameters:
        string              (string)            Input binary string
        raw                 (boolean)           Return as bytes

    Returns:
        string              (string/bytes)      decoded output
    '''
    if re.search('[^01]', string):
        raise VveException("Input string is not binary.")

    b_array = bytearray()
    for i in range(0, len(string), 8):
        integer = int(string[i:i+8], 2)
        b_array.append(integer)

    if raw:
        return bytes(b_array)

    try:
        return b_array.decode('utf-8')
    except:
        raise VveException("Decoded result cannot be encoded as UTF-8.")


def encode_hex_string(data):
    '''
    Accepts a string or bytes input and converts it into a hex-string
    (\\x..\\x..\\x..). 

    Parameters:
        data                (string/bytes)      Input data

    Returns:
        return_value        (string)            Formatted hex output
    '''
    if not isinstance(data, bytes):
        data = data.encode('utf-8')

    hex_form = data.hex()
    return_value = ''

    for i in range(0, len(hex_form), 2):
        return_value += '\\x' + hex_form[i:i+2]

    return return_value


def decode_hex_string(string, raw=False):
    '''
    Takes a hex string (\\x..\\x..\\x..) as input and converts it back into
    either an utf-8 formatted string or a raw bytes value.

    Parameters:
        string              (string)            Input hex string
        raw                 (boolean)           Return as bytes

    Returns:
        string              (string/bytes)      Decoded output
    '''
    plain = string.replace('\\x', '')

    try:
        b_array = bytearray.fromhex(plain)
    except:
        raise VveException("Input is no valid hex string.")

    if raw:
        return bytes(b_array)

    try: 
        return b_array.decode('utf-8')
    except:
        raise VveException("Decoded result cannot be encoded as UTF-8.")
        

def encode_hex(data):
    '''
    Takes either a string or a raw bytes value as input and converts it to hex.
    If input is string, it is utf-8 decoded first and then each byte will be
    converted into a hex number. The single hex numbers will then be concatenated.

    Parameters:
        data                (string/bytes)      Input data

    Returns:
        string              (string)            Hex formatted output
    '''
    if not isinstance(data, bytes):
        data = data.encode('utf-8')

    return data.hex()


def decode_hex(string, raw=False):
    '''
    Takes a stream of hex numbers (e.g. A01FE92...) and converts it, either
    into an utf-8 formatted string or a raw bytes value.

    Parameters:
        string              (string)            Input hex stream
        raw                 (boolean)           Return as bytes

    Returns:
        string              (string/bytes)      UTF-8 formatted output
    '''
    try: 
        b_array = bytearray.fromhex(string)
    except:
        raise VveException('Input is not in hex format.')

    if raw:
        return bytes(b_array)

    try: 
        return b_array.decode('utf-8')
    except:
        raise VveException("Decoded result cannot be encoded as UTF-8.")


def encode_url_full(data):
    '''
    Takes a string or raw bytes as input and applies URL encoding to
    each character. If input is string, it is treated as utf-8 and
    multibyte characters are encoded as seperate URL encoded characters.

    Parameters:
        data                (string/bytes)      Input data

    Returns:
        string              (string)            URL encoded output
    '''
    if not isinstance(data, bytes):
        data = data.encode('utf-8')

    hex_form = data.hex()
    return_value = ''

    for i in range(0, len(hex_form), 2):
        return_value += '%' + hex_form[i:i+2]

    return return_value


def encode_url(data):
    '''
    Applies URL encoding to the input data for URL special characters.
    Input data can be specified as string or raw bytes.

    Parameters:
        data                (string/bytes)      Input data

    Returns:
        string              (string)            URL encoded output
    '''
    return urllib.parse.quote_plus(data)


def decode_url(string, raw=False):
    '''
    Applies URL decoding to the input string. Output can be obtained as
    utf-8 string or raw byes.

    Parameters:
        string              (string)            Input string
        raw                 (boolean)           Return as bytes

    Returns:
        string              (string/bytes)      URL decoded output
    '''
    decoded = urllib.parse.unquote_plus(string)

    if raw:
        return decoded.encode('utf-8')

    return decoded


def encode_xml(string):
    '''
    Applies XML encoding to the input string for XML special characters.

    Parameters:
        string              (string)            Input string

    Returns:
        string              (string)            XML encoded output
    '''
    if isinstance(string, bytes):
        raise VveException("XML encoding is only supported for UTF-8 data.")

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


def encode_html_full(data):
    '''
    Applies HTML encoding to the complete input data. The input data
    can be specified as string or bytes. If specified as bytes, it is
    treated as utf-8 and each byte gets encoded seperately.

    Parameters:
        string              (string/bytes)      Input string

    Returns:
        string              (string)            HTML encoded output
    '''
    if not isinstance(data, bytes):
        data = data.encode('utf-8')

    hex_form = data.hex()
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
    if isinstance(string, bytes):
        raise VveException("HTML encoding is only supported for UTF-8 data.")

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


def encode_ascii(byte_value):
    '''
    Takes a bytes object and converts each ASCII byte into its character representation.
    Bytes that are out of the ASCII range are displayed as escape sequence \\xXX. This
    encoding can only be applied on bytes input and is only ment to be used in 
    ChangeEncoding operations.

    Paramaters:
        byte_value          (bytes)             Input data

    Returns:
        ascii_value         (string)            ASCII output
    '''
    result = ''
    for byte in byte_value:

        if byte > 0x1f and byte < 0x7f:
            result += chr(byte)

        else:
            b_hex = "\\x{:02x}".format(byte)
            b_hex = b_hex.replace('0x', '\\x')
            result += b_hex

    return result


def decode_ascii(string, raw=False):
    '''
    Opposite operation to encode_ascii. Searches for \\xXX sequences inside the input
    string and converts them to their raw byte value. Afterwards, the whole string
    is converted to bytes. If raw=True, this bytes object is returned. Otherwise, the
    bytearray will be decoded as utf-8.

    Paramaters:
        string              (string)            Input string
        raw                 (boolean)           True -> type(output)=bytes

    Returns:
        decoded             (string/bytes)      Decoded output
    '''
    replacer = lambda x: chr(int(x.group().replace('\\x', ''), 16))
    string = re.sub(r'\\x[0-9a-fA-F]{2}', replacer, string)

    decoded = b''
    for char in string:
        decoded += bytes([ord(char)])

    if raw:
        return decoded

    return result.decode('utf-8')


local_functions = locals()


def chain(funcref_1, funcref_2):
    '''
    Helper function that chains two function calls together. This is required for
    implementing the change_encoding function, because of design decisions that were
    taken earlier in this project. funcref_1 is expected to be a decoding function,
    whereas funcref_2 is expected to be an encoding function. The chain function
    returns the combined calls funcref_2(funcref_1(data, raw=True)). Using the
    raw parameter is crucial, as change_encoding should also allow changing encodings
    on non UTF-8 formatted data.

    Paramaters:
        funcref_1           (funcref)           Reference to a decoding function
        funcref_2           (funcref)           Reference to an encoding function

    Returns:
        chained             (funcref)           Reference to the chained function
    '''
    def chained(data):
        decoded = funcref_1(data, raw=True)
        encoded = funcref_2(decoded)
        return encoded

    return chained


def change_encoding(decode_function, encode_function, visualmode):
    '''
    Applies the combination of {decode_function} (decoding function that accepts the
    {raw} paramater) and {encode_function} to the last visual selection. The last
    visual selection is then replaced by the corresponding result.

    Parameters:
        decode_function     (string)            Name of the decoding function
        encode_function     (string)            Name of the encoding function
        visualmode          (string)            Mode of last visual selection (v|V|^V).

    Returns:
        None
    '''
    funcref_encode = local_functions[encode_function]
    funcref_decode = local_functions[decode_function]
    funcref_chained = chain(funcref_decode, funcref_encode)
    vve.visual.visual_apply(funcref_chained, visualmode)

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
