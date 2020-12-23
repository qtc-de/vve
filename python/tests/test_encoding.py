#!/usr/bin/python3

import pytest
import vve.encode as vve


@pytest.mark.parametrize('key, value', [('subsetneqq;', '⫋'), ('DoubleContourIntegral;', '∯')])
def test_get_entity(key, value):
    '''
    Test the vve.get_entity function. This test should always work, as the function performs
    just a lookup on a dictionary within pythons html package.
    '''
    assert vve.get_entity(key) == value


@pytest.mark.parametrize('string, result', [('He\xffllo\x0a', b'\x48\x65\xff\x6C\x6C\x6F\x0a'),
                                            ('•.•', b'\xe2\x80\xa2\x2e\xe2\x80\xa2'),
                                            ])
def test_encode_mixed(string, result):
    '''
    Test the vve.encode_mixed function. To test this correctly one needs one string that contains
    high valued 'ascii' characters and one that contains some unicode.
    '''
    assert vve.encode_mixed(string) == result


@pytest.mark.parametrize('string, result', [('He•llo•', 'SGXigKJsbG/igKI='),
                                            (b'\xe2\x80\xa2\x2e\xe2\x80\xa2', '4oCiLuKAog=='),
                                            ])
def test_encode_b64(string, result):
    '''
    Test the vve.encode_base64 function. This test should always pass, as the underlying vve function just
    uses pythons b64 module.
    '''
    assert vve.encode_base64(string) == result


@pytest.mark.parametrize('string, result, raw', [('SGXigKJsbG/igKI=', 'He•llo•', False),
                                                 ('4oCiLuKAog', b'\xe2\x80\xa2\x2e\xe2\x80\xa2', True),
                                                 ])
def test_decode_b64(string, result, raw):
    '''
    Test the vve.decode_base64 function. This test should always pass, as the underlying vve function just
    uses pythons b64 module. Additionally, autocorrection of the padding is tested.
    '''
    assert vve.decode_base64(string, raw) == result


@pytest.mark.parametrize('string, result', [('Hello', '0100100001100101011011000110110001101111'),
                                            ('•', '111000101000000010100010'),
                                            ])
def test_encode_binary(string, result):
    '''
    Test the vve.encode_binary function.
    '''
    assert vve.encode_binary(string) == result


@pytest.mark.parametrize('string, result, raw', [('0100100001100101011011000110110001101111', 'Hello', False),
                                                 ('111000101000000010100010', '•', False),
                                                 ('11111111', b'\xff', True),
                                                 ])
def test_decode_binary(string, result, raw):
    '''
    Test the vve.decode_binary function.
    '''
    assert vve.decode_binary(string, raw) == result


@pytest.mark.parametrize('string, result', [('Hello', '\\x48\\x65\\x6c\\x6c\\x6f'), ('•', '\\xe2\\x80\\xa2')])
def test_encode_hex_string(string, result):
    '''
    Test the vve.encode_hex_string function.
    '''
    assert vve.encode_hex_string(string) == result


@pytest.mark.parametrize('string, result, raw', [('\\x48\\x65\\x6c\\x6c\\x6f', 'Hello', False),
                                                 ('\\xe2\\x80\\xa2', '•', False),
                                                 ('\\xff', b'\xff', True),
                                                 ])
def test_decode_hex_string(string, result, raw):
    '''
    Test the vve.decode_hex_string function.
    '''
    assert vve.decode_hex_string(string, raw) == result


@pytest.mark.parametrize('string, result', [('Hello', '48656c6c6f'), ('•', 'e280a2')])
def test_encode_hex(string, result):
    '''
    Test the vve.encode_hex function.
    '''
    assert vve.encode_hex(string) == result


@pytest.mark.parametrize('string, result, raw', [('48656c6c6f', 'Hello', False),
                                                 ('e280a2', '•', False),
                                                 ('ff', b'\xff', True),
                                                 ])
def test_decode_hex(string, result, raw):
    '''
    Test the vve.decode_hex function.
    '''
    assert vve.decode_hex(string, raw) == result


@pytest.mark.parametrize('string, result', [('H l%&', 'H+l%25%26'), ('•.•', '%E2%80%A2.%E2%80%A2')])
def test_encode_url(string, result):
    '''
    Test the vve.encode_url function.
    '''
    assert vve.encode_url(string) == result


@pytest.mark.parametrize('string, result', [('H l%&', '%48%20%6c%25%26'), ('•.•', '%E2%80%A2%2E%E2%80%A2'.lower())])
def test_encode_url_full(string, result):
    '''
    Test the vve.encode_url_full function.
    '''
    assert vve.encode_url_full(string) == result


@pytest.mark.parametrize('string, result, raw', [('%48%20%6c%25%26', 'H l%&', False),
                                                 ('%E2%80%A2%2E%E2%80%A2', '•.•', False),
                                                 ('%ff', b'\xef\xbf\xbd', True),
                                                 ])
def test_decode_url(string, result, raw):
    '''
    Test the vve.decode_url function.
    '''
    assert vve.decode_url(string, raw) == result


@pytest.mark.parametrize('string, result, raw', [('%48%20%6c%25%26', 'H l%&', False),
                                                 ('%E2%80%A2.%E2%80%A2', '•.•', False),
                                                 ('%ff', b'\xff', True),
                                                 ])
def test_decode_url_full(string, result, raw):
    '''
    Test the vve.decode_url_full function.
    '''
    assert vve.decode_url_full(string, raw) == result


@pytest.mark.parametrize('string, result', [('H<l>&', 'H&lt;l&gt;&amp;'), ('•.•', '•.•')])
def test_encode_html(string, result):
    '''
    Test the vve.encode_html function.
    '''
    assert vve.encode_html(string) == result


@pytest.mark.parametrize('string, result', [('H<l>&', '&#x48;&#x3c;&#x6c;&#x3e;&#x26;'),
                                            ('•.•', '&#xe2;&#x80;&#xa2;&#x2e;&#xe2;&#x80;&#xa2;'),
                                            ])
def test_encode_html_full(string, result):
    '''
    Test the vve.encode_html_full function.
    '''
    assert vve.encode_html_full(string) == result


@pytest.mark.parametrize('string, result', [('H&lt;l&gt;&amp;', 'H<l>&'), ('&aaaa&lt;&gt;aaaa;', '&aaaa<>aaaa;')])
def test_decode_html(string, result):
    '''
    Test the vve.decode_html function.
    '''
    assert vve.decode_html(string) == result


@pytest.mark.parametrize('string, result, raw', [('H&lt;l&gt;&amp;', 'H<l>&', False),
                                                 ('&#xe2;&#x80;&#xa2;&#x2e;&#xe2;&#x80;&#xa2;', '•.•', False),
                                                 ('&#xff;', b'\xff', True),
                                                 ])
def test_decode_html_full(string, result, raw):
    '''
    Test the vve.decode_html_full function.
    '''
    assert vve.decode_html_full(string, raw) == result


@pytest.mark.parametrize('string, result', [('H<l>&', 'H&lt;l&gt;&amp;'), ('•.•', '•.•')])
def test_encode_xml(string, result):
    '''
    Test the vve.encode_xml function.
    '''
    assert vve.encode_xml(string) == result


@pytest.mark.parametrize('string, result', [('H<l>&', '&#x48;&#x3c;&#x6c;&#x3e;&#x26;'),
                                            ('•.•', '&#xe2;&#x80;&#xa2;&#x2e;&#xe2;&#x80;&#xa2;'),
                                            ])
def test_encode_xml_full(string, result):
    '''
    Test the vve.encode_xml_full function.
    '''
    assert vve.encode_xml_full(string) == result


@pytest.mark.parametrize('string, result', [('H&lt;l&gt;&amp;', 'H<l>&'), ('&aaaa&lt;&gt;aaaa;', '&aaaa<>aaaa;')])
def test_decode_xml(string, result):
    '''
    Test the vve.decode_xml function.
    '''
    assert vve.decode_xml(string) == result


@pytest.mark.parametrize('string, result, raw', [('H&lt;l&gt;&amp;', 'H<l>&', False),
                                                 ('&#xe2;&#x80;&#xa2;&#x2e;&#xe2;&#x80;&#xa2;', '•.•', False),
                                                 ('&#xff;', b'\xff', True),
                                                 ])
def test_decode_xml_full(string, result, raw):
    '''
    Test the vve.decode_xml_full function.
    '''
    assert vve.decode_xml_full(string, raw) == result


@pytest.mark.parametrize('string, result', [('Ha•o', 'Ha\\xe2\\x80\\xa2o'), (b'Ha\xff\xffo', 'Ha\\xff\\xffo')])
def test_encode_ascii(string, result):
    '''
    Test the vve.encode_ascii function.
    '''
    assert vve.encode_ascii(string) == result


@pytest.mark.parametrize('string, result, raw', [('Ha\\xe2\\x80\\xa2o', 'Ha•o', False),
                                                 ('Ha\\xff\\xffo', b'Ha\xff\xffo', True),
                                                 ])
def test_decode_ascii(string, result, raw):
    '''
    Test the vve.decode_ascii function.
    '''
    assert vve.decode_ascii(string, raw) == result
