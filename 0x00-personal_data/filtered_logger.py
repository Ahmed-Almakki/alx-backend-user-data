#!/usr/bin/evn python3
""" Regex-ing """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ search for fields and changge it to unreadabl formate"""
    for fl in fields:
        message = re.sub(r"(?<=" + re.escape(fl) + r"=)[^" + separator + r"]+",
                         redaction, message)
    return message
