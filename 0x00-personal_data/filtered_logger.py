#!/usr/bin/evn python3
""" Regex-ing """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ search for fields and changge it to unreadabl formate"""
    for f in fields:
        message = re.sub(fr"(?<={f}=)[^{separator}]+", redaction, message)
    return message
