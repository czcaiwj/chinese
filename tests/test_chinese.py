# coding: utf-8

from nihao import api

a = '这里包含了中文abcded'
b = 'there is no chinese here'

def test_chinese1():
    result = api.containChinese(a)
    expected = True
    assert result == expected

def test_chinese2():
    result = api.containChinese(b)
    expected = False
    assert result == expected
