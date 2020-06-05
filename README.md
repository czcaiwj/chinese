# 检测字符串中是否包含中文字符


## 概述
Unicode 是全球文字统一编码。它把世界上的各种文字的每一个字符指定唯一编码，实现跨语种、跨平台的应用。

中文用户最常接触的是汉字 Unicode 编码。中文字符数量巨大，日常使用的汉字数量有数千个，再加上生僻字，数量达到数万个。下面这个表格将中文字符集的 Unicode 编码范围列出：

字符集 | 字数 | Unicode编码范围
------------ | ------------- | -------------
基本汉字 | 20902 | 4E00-9FA5
基本汉字补充 | 74 | 9FA6-9FEF
扩展A | 6582 | 3400-4DB5
扩展B | 42711 | 20000-2A6D6
扩展C | 4149 | 2A700-2B734
扩展D | 222 | 2B740-2B81D
扩展E | 5762 | 2B820-2CEA1
扩展F | 7473 | 2CEB0-2EBE0
扩展G | 4939 | 30000-3134A
康熙部首 | 214 | 2F00-2FD5
部首扩展 | 115 | 2E80-2EF3
兼容汉字 | 477 | F900-FAD9
兼容扩展 | 542 | 2F800-2FA1D
PUA(GBK)部件 | 81 | E815-E86F
部件扩展 | 452 | E400-E5E8
PUA增补 | 207 | E600-E6CF
汉字笔画 | 36 | 31C0-31E3
汉字结构 | 12 | 2FF0-2FFB
汉语注音 | 43 | 3105-312F
注音扩展 | 22 | 31A0-31BA
〇 | 1 | 3007

根据上述字符范围，可以使用本工具来识别给定字符串是否含义中文字符。

## 安装方法
pip install nihao

## 使用方法
import nihao
a = '这里包含了中文abcded'
b = 'there is no chinese here'

def test_chinese1():
    result = nihao.containChinese(a)
    expected = True
    assert result == expected

def test_chinese2():
    result = nihao.containChinese(b)
    expected = False
    assert result == expected
