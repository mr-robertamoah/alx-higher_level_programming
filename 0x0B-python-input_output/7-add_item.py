#!/usr/bin/python3

"""
A script to load from and/or dump to
a file
"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
new_list_items = sys.argv[1:]
items = []

try:
    file = open(filename, 'r')
    content = file.read()
    file.close()
    if len(content):
        items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

for item in new_list_items:
    items.append(item)

save_to_json_file(items, filename)
