#!/usr/bin/python3

import pytest
import vve.numbers as vve


@pytest.mark.parametrize('string, hexval', [
                                            ('1337', '0x0539'),
                                            ('13371337', '0xcc07c9'),
                                            ('0x13371337', '0x13371337'),
                                            ('0o1337', '0x02df'),
                                            ('0b1001100110111', '0x1337'),
                                            ('\\x13\\x37\\x13\\x37', '0x13371337')
                                            ])
def test_to_hex(string, hexval):
    '''
    Test vve.to_hex function.
    '''
    assert vve.to_hex(string) == hexval


@pytest.mark.parametrize('string, binval', [
                                            ('1337', '0b0000010100111001'),
                                            ('13371337', '0b110011000000011111001001'),
                                            ('0x13371337', '0b00010011001101110001001100110111'),
                                            ('0o1337', '0b0000001011011111'),
                                            ('0b1001100110111', '0b0001001100110111'),
                                            ('\\x13\\x37\\x13\\x37', '0b00010011001101110001001100110111'),
                                            ])
def test_to_bin(string, binval):
    '''
    Test vve.to_bin function.
    '''
    assert vve.to_bin(string) == binval


@pytest.mark.parametrize('string, octval', [
                                            ('1337', '0o2471'),
                                            ('13371337', '0o63003711'),
                                            ('0x13371337', '0o2315611467'),
                                            ('0o1337', '0o1337'),
                                            ('0b1001100110111', '0o11467'),
                                            ('\\x13\\x37\\x13\\x37', '0o2315611467'),
                                            ])
def test_to_oct(string, octval):
    '''
    Test vve.to_oct function.
    '''
    assert vve.to_oct(string) == octval


@pytest.mark.parametrize('string, decval', [
                                            ('0x1337', '4919'),
                                            ('0x13371337', '322376503'),
                                            ('0o1337', '735'),
                                            ('0b1001100110111', '4919'),
                                            ('\\x13\\x37\\x13\\x37', '322376503'),
                                            ])
def test_to_dec(string, decval):
    '''
    Test vve.to_dec function.
    '''
    assert vve.to_dec(string) == decval


@pytest.mark.parametrize('string, hexstring', [
                                               ('1337', '\\x05\\x39'),
                                               ('13371337', '\\xcc\\x07\\xc9'),
                                               ('0x13371337', '\\x13\\x37\\x13\\x37'),
                                               ('0o1337', '\\x02\\xdf'),
                                               ('0b1001100110111', '\\x13\\x37'),
                                               ])
def test_to_hex_string(string, hexstring):
    '''
    Test vve.to_hex_string function.
    '''
    assert vve.to_hex_string(string) == hexstring


@pytest.mark.parametrize('string, number', [
                                            ('1337', 1337),
                                            ('0x13371337', 0x13371337),
                                            ('0o1337', 0o1337),
                                            ('0b1001100110111', 0b1001100110111),
                                            ('\\x13\\x37\\x13\\x37', 0x13371337),
                                            ])
def test_to_bin(string, number):
    '''
    Test vve.to_number function.
    '''
    assert vve.to_number(string) == number
