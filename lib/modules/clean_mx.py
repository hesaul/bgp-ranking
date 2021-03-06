#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    CleanMX parser
    ~~~~~~~~~~~~~~

    The default parser of CleanMX lists
"""

import re
from helper import new_entry


def parser(filename, listname, date):
    """
        Parse the list
    """
    with open(filename, 'r') as f :
        for line in f:
            ip = re.findall('<(?:ip|review)>((?:\d{1,3}\.){3}\d{1,3})<.*',line)
            if len(ip) == 0:
                continue
            new_entry(ip = ip[0], source = listname, timestamp = date)
    return date
