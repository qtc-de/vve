#!/usr/bin/python3

import sys
import pytest
from io import StringIO

import vve.strings as vve


@pytest.mark.parametrize('string, formatting', [
                                            ('aabbcc', 'plain'),
                                            ('\\xaa\\xbb\\xcc', 'formatted'),
                                            ('xxyyzz', None),
                                            ('\\xxx\\xyy\\xzz', None),
                                            ('aabbc', None),
                                            ('\\xaa\\xbb\\xc', None)
                                            ])
def test_get_hex_format(string, formatting):
    '''
    Test vve._get_hex_format function.
    '''
    assert vve._get_hex_format(string) == formatting


@pytest.mark.parametrize('string, length', [
                                            ('aabbcc', '3\n'),
                                            ('0xaabbcc', '3\n'),
                                            ('\\xaa\\xbb\\xcc', '3\n'),
                                            ])
def test_string_length_hex(string, length):
    '''
    Test vve.string_length_hex function.
    '''
    orig_stdout = sys.stdout
    sys.stdout = new_stdout = StringIO()

    vve.string_length_hex(string)
    result = new_stdout.getvalue()

    sys.stdout = orig_stdout
    assert result == length


@pytest.mark.parametrize('string, result', [
                                            ('aabbcc', 'ccbbaa'),
                                            ('0xaabbcc', '0xccbbaa'),
                                            ('\\xaa\\xbb\\xcc', '\\xcc\\xbb\\xaa'),
                                            ])
def test_swap_endian(string, result):
    '''
    Test vve.swap_endian function.
    '''
    assert vve.swap_endian(string) == result


@pytest.mark.parametrize('string, anchor', [
                                            ('Hello World', '#hello-world'),
                                            ('Hello World 2', '#hello-world-2'),
                                            ])
def test_string_markdown_anchor(string, anchor):
    '''
    Test vve.string_markdown_anchor function.
    '''
    assert vve.string_markdown_anchor(string) == anchor


@pytest.mark.parametrize('string, anchor', [
                                            ('Hello World', '[Hello World](#hello-world)'),
                                            ('Hello World 2', '[Hello World 2](#hello-world-2)'),
                                            ])
def test_string_markdown_anchor_reference(string, anchor):
    '''
    Test vve.string_markdown_anchor_reference function.
    '''
    assert vve.string_markdown_anchor_reference(string) == anchor


@pytest.mark.parametrize('string, snake_case', [
                                            ('helloWorld', 'hello_world'),
                                            ('reallyLongFunctionName', 'really_long_function_name'),
                                            ])
def test_string_snake_case(string, snake_case):
    '''
    Test vve.string_snake_case function.
    '''
    assert vve.string_snake_case(string) == snake_case


@pytest.mark.parametrize('string, camel_case', [
                                            ('hello_world', 'helloWorld'),
                                            ('really_long_function_name', 'reallyLongFunctionName'),
                                            ])
def test_string_camel_case(string, camel_case):
    '''
    Test vve.string_camel_case function.
    '''
    assert vve.string_camel_case(string) == camel_case
