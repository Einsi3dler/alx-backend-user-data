#!/usr/bin/env python3
"""
Logging File
"""
from typing import List
import re
import logging
from os import environ
import mysql.connector



def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ Returns an redacted log file"""
    