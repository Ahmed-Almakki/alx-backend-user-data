#!/usr/bin/evn python3
""" loggin file that contain obfuscated data """
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Replacing certen filed with obfuscated data """
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                         f'{f}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initilaizing with field paramter"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ formats a LogRecord using filter function"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ createing a logger file """
    logger = logging.getLogger("user_data")
    logger.propagate = False
    logger.setLevel(logging.INFO)

    st = logging.StreamHandler()
    st.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(st)
    return logger
