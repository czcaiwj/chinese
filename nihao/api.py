# coding: utf-8

import re

def containChinese(content: str) -> bool:
    """ 判断内容是否含有中文字符
    Arguments:
        content {string} -- 要检测的内容

    Returns:
        {bool} -- 是否包含中文
    """

    zh_pattern = re.compile(
        u'([\u4E00-\u9FA5]|[\u9FA6-\u9FEF]|[\u3400-\u4DB5]|[\U00020000-\U0002A6D6]|[\U0002A700-\U0002B734]|[\U0002B740-\U0002B81D]|[\U0002B820-\U0002CEA1]|[\U0002CEB0-\U0002EBE0]|[\U00030000-\U0003134A]|[\u2F00-\u2FD5]|[\u2E80-\u2EF3]|[\uF900-\uFAD9]|[\U0002F800-\U0002FA1D]|[\uE815-\uE86F]|[\uE400-\uE5E8]|[\uE600-\uE6CF]|[\u31C0-\u31E3]|[\u2FF0-\u2FFB]|[\u3105-\u312F]|[\u31A0-\u31BA]|[\u3007])+'
    )
    match = zh_pattern.search(content)
    return match is not None
