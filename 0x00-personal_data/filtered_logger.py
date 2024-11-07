#!/usr/bin/evn python3
""" Regex-ing """
import re
from typing import List


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}

def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ search for fields and changge it to unreadabl formate"""
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
