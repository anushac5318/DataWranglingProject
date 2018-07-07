#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
from collections import defaultdict
import re

osm_file = open("sample.osm", "r")

postalcode_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)
postalcode_types = defaultdict(int)


# Adds the postalcodes to dictionary
def audit_postalcode_type(postalcode_types, postal_code):
    postalcode_types[postal_code] += 1

# sorting keys in dictionary
def print_sorted_dict(d):
    keys = d.keys()
    keys = sorted(keys, key=lambda s: s.lower())
    for k in keys:
        v = d[k]
        print "%s: %d" % (k, v)

# function returns if it's a tag and key is addr:postcode
def is_postcode(elem):
    return (elem.tag == "tag") and (elem.attrib['k'] == "addr:postcode")

# Auditing on osm file
def audit():
    for event, elem in ET.iterparse(osm_file):
        if is_postcode(elem):
            audit_postalcode_type(postalcode_types, elem.attrib['v'])
    print_sorted_dict(postalcode_types)


if __name__ == '__main__':
    audit()
